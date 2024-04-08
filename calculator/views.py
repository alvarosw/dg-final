import os
import requests
from django.shortcuts import render
from .forms import CalculatorForm

def calculator(request):
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        
        if form.is_valid():
            response = requests.post(
                f"{os.environ['API_HOST']}/calculator/",
                data=form.cleaned_data
            )

            if response.status_code == 200:
                return render(
                    request, 
                    'result.html', 
                    response.json()
                )

    form = CalculatorForm()
    return render(request, 'form.html', { 'form': form })
