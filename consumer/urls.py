from django.urls import path
from .views import (
  consumer_list,
  consumer_create,
)

urlpatterns = [
    path("", consumer_list),
    path("create/", consumer_create),
]
