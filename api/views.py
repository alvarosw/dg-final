from rest_framework.views import APIView
from rest_framework.response import Response
from .calculator import calculate
from rest_framework import status
from .serializers import CalculatorInputSerializer

class CalculatorAPIView(APIView):
    def post(self, request):
        serializer = CalculatorInputSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            consumption = [data['consumption1'], data['consumption2'], data['consumption3']]
            distributor_tax = data['distributor_tax']
            tax_type = data['tax_type']

            try:
                (
                    annual_savings,
                    monthly_savings,
                    applied_discount,
                    coverage
                ) = calculate(consumption, distributor_tax, tax_type)
                
                return Response({ 
                    'annual_savings': annual_savings, 
                    'monthly_savings': monthly_savings, 
                    'applied_discount': applied_discount, 
                    'coverage': coverage
                })
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)