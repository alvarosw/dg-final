from django.urls import path
from .views import CalculatorAPIView, ConsumerAPIView

urlpatterns = [
    path("calculator/", CalculatorAPIView.as_view()),
    path("consumer/", ConsumerAPIView.as_view()),
]
