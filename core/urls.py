from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("api/", include('api.urls'), name='api'),
    path("admin/", admin.site.urls),
    path("consumer/", include('consumer.urls'), name='consumer'),
    path("calculator/", include('calculator.urls'), name='calculator'),
]
