from django.shortcuts import render
from .calculator_python import calculate
from .forms import CalculatorForm

def calculator(request):
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        
        if form.is_valid():
            (
                annual_savings,
                monthly_savings,
                applied_discount,
                coverage
            ) = calculate(
                [
                    form.cleaned_data['consumption1'],
                    form.cleaned_data['consumption2'],
                    form.cleaned_data['consumption3']
                ],
                form.cleaned_data['distributor_tax'],
                form.cleaned_data['tax_type']
            )

            return render(
                request, 
                'result.html', 
                {
                    'annual_savings': annual_savings,
                    'monthly_savings': monthly_savings,
                    'applied_discount': applied_discount,
                    'coverage': coverage
                })

    form = CalculatorForm()
    return render(request, 'form.html', { 'form': form })
