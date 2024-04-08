from django.urls import path
from .views import (
    CalculatorAPIView,
    ConsumerAPIView,
    DiscountRuleAPIView,
    DiscountCoverageRuleAPIView,
)

urlpatterns = [
    path("calculator/", CalculatorAPIView.as_view()),
    path("consumer/", ConsumerAPIView.as_view()),
    path("consumer/<int:pk>/", ConsumerAPIView.as_view()),
    path("discount_rule/", DiscountRuleAPIView.as_view()),
    path("discount_coverage_rule/", DiscountCoverageRuleAPIView.as_view()),
]
