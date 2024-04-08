from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .calculator import calculate
from .serializers import CalculatorInputSerializer, ConsumerSerializer
from consumer.models import Consumer


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
