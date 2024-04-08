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
            discount_rule = get_discount_rule(
                form.cleaned_data["consumer_type"], form.cleaned_data["consumption"]
            )
            form.cleaned_data["discount_rule"] = discount_rule
            del form.cleaned_data["consumer_type"]
            Consumer.objects.create(**form.cleaned_data)

            return redirect("../consumer")
        else:
            return render(request, "create.html", {"form": form})

    form = ConsumerCreationForm()
    return render(request, "create.html", {"form": form})


def home(request):
    return redirect("calculator/")


def get_discount_rule(consumer_type, consumption):
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
