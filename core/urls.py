from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def root_view(_):
    return redirect('calculator/')

urlpatterns = [
    path("api/", include('api.urls'), name='api'),
    path("admin/", admin.site.urls),
    path("consumer/", include('consumer.urls'), name='consumer'),
    path("calculator/", include('calculator.urls'), name='calculator'),

    path("", root_view),
]
