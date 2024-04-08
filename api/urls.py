from django.urls import path
from .views import CalculatorAPIView

urlpatterns = [
    path("calculator/", CalculatorAPIView.as_view()),
]
