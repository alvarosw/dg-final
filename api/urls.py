from django.urls import path
from .views import (
    CalculatorAPIView,
    ConsumerAPIView,
    DiscountRuleAPIView,
    DiscountCoverageRuleAPIView,
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(title="Digital Grid API", default_version="v1"),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("calculator/", CalculatorAPIView.as_view()),
    path("consumer/", ConsumerAPIView.as_view()),
    path("consumer/<int:pk>/", ConsumerAPIView.as_view()),
    path("discount_rule/", DiscountRuleAPIView.as_view()),
    path("discount_coverage_rule/", DiscountCoverageRuleAPIView.as_view()),
]
