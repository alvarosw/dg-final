from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .calculator import calculate
from consumer.models import Consumer, ConsumerType, ConsumptionRange, DiscountRules
from .serializers import (
    CalculatorInputSerializer,
    ConsumerSerializer,
    ConsumerSaveSerializer,
    DiscountRuleSerializer,
)


class CalculatorAPIView(APIView):
    def post(self, request):
        serializer = CalculatorInputSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            consumption = [
                data["consumption1"],
                data["consumption2"],
                data["consumption3"],
            ]
            distributor_tax = data["distributor_tax"]
            tax_type = data["tax_type"]

            try:
                (annual_savings, monthly_savings, applied_discount, coverage) = (
                    calculate(consumption, distributor_tax, tax_type)
                )

                return Response(
                    {
                        "annual_savings": annual_savings,
                        "monthly_savings": monthly_savings,
                        "applied_discount": applied_discount,
                        "coverage": coverage,
                    }
                )
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConsumerAPIView(APIView):
    def get(self, request):
        consumer_type = request.GET.get("consumer_type")
        consumption_range = request.GET.get("consumption_range")

        consumers = Consumer.objects.all().select_related("discount_rule")

        if consumer_type:
            consumers = consumers.filter(discount_rule__consumer_type=consumer_type)

        if consumption_range:
            consumers = consumers.filter(
                discount_rule__consumption_range=consumption_range
            )

        data = []
        for consumer in consumers:
            monthly_savings = (
                consumer.consumption
                * consumer.distributor_tax
                * consumer.discount_rule.discount_value
                * consumer.discount_rule.cover_value
            )

            consumer_data = ConsumerSerializer(consumer).data

            data.append(
                {
                    **consumer_data,
                    "applied_discount": consumer.discount_rule.discount_value,
                    "discount_coverage": consumer.discount_rule.cover_value,
                    "monthly_savings": round(monthly_savings, 2),
                    "annual_savings": round(monthly_savings * 12, 2),
                }
            )

        return Response({"consumers": data})

    def post(self, request):
        serializer = ConsumerSaveSerializer(data=request.data)
        if serializer.is_valid():
            consumer_type = serializer.validated_data["consumer_type"]
            consumption = serializer.validated_data["consumption"]
            discount_rule = self.get_discount_rule(consumer_type, consumption)

            serializer.validated_data["discount_rule"] = discount_rule
            del serializer.validated_data["consumer_type"]

            Consumer.objects.create(**serializer.validated_data)
            serializer.validated_data["discount_rule"] = DiscountRuleSerializer(
                discount_rule
            ).data

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            consumer = Consumer.objects.get(pk=pk)
        except Consumer.DoesNotExist:
            return Response(
                {"error": "Consumer not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = ConsumerSaveSerializer(consumer, data=request.data)
        if serializer.is_valid():
            consumer_type = serializer.validated_data["consumer_type"]
            consumption = serializer.validated_data["consumption"]
            discount_rule = self.get_discount_rule(consumer_type, consumption)

            serializer.validated_data["discount_rule"] = discount_rule
            del serializer.validated_data["consumer_type"]

            serializer.save()
            serializer.validated_data["discount_rule"] = DiscountRuleSerializer(
                discount_rule
            ).data

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            consumer = Consumer.objects.get(pk=pk)
        except Consumer.DoesNotExist:
            return Response(
                {"error": "Consumer not found"}, status=status.HTTP_404_NOT_FOUND
            )

        consumer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_discount_rule(self, consumer_type, consumption):
        consumer_type: ConsumerType = consumer_type
        consumption = int(consumption)

        if consumption < 10000:
            consumption_range = ConsumptionRange.LESS_THAN_10K.value
        elif 10000 <= consumption <= 20000:
            consumption_range = ConsumptionRange.BETWEEN_10K_AND_20K.value
        else:
            consumption_range = ConsumptionRange.MORE_THAN_20K.value

        return DiscountRules.objects.get(
            consumer_type=consumer_type, consumption_range=consumption_range
        )


class DiscountRuleAPIView(APIView):
    def get(self, request):
        discount_rules = DiscountRules.objects.all()
        data = DiscountRuleSerializer(discount_rules, many=True).data

        return Response({"discount_rules": data})


class DiscountCoverageRuleAPIView(APIView):
    def get(self, request):
        return Response(
            {
                "< 10.000 kWh": "90%",
                ">= 10.000 kWh e <= 20.000 kWh": "95%",
                "> 20.000 kWh": "99%",
            }
        )
