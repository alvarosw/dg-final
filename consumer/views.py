import os
import requests
from django.shortcuts import render, redirect
from consumer.models import Consumer, DiscountRules, ConsumerType, ConsumptionRange
from .forms import ConsumerFilterForm, ConsumerCreationForm


def consumer_list(request):
    filter_form = ConsumerFilterForm(request.GET)

    if filter_form.is_valid():
        response = requests.get(
            f"{os.environ['API_HOST']}/consumer/", params=filter_form.cleaned_data
        )
    else:
        response = requests.get(f"{os.environ['API_HOST']}/consumer/")

    return render(request, "list.html", {**response.json(), "filter_form": filter_form})


def consumer_create(request):
    if request.method == "POST":
        form = ConsumerCreationForm(request.POST)
        if form.is_valid():
            response = requests.post(
                f"{os.environ['API_HOST']}/consumer/", data=form.cleaned_data
            )
            if response.status_code == 201:
                return redirect("/")

        return render(request, "create.html", {"form": form})

    form = ConsumerCreationForm()
    return render(request, "create.html", {"form": form})
