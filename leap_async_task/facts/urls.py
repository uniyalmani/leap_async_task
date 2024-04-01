from django.contrib import admin
from django.urls import path
from .views import health_check, fetch_fact_view, get_fact

urlpatterns = [
    path('health_check/', health_check, name='health_check'),
    path('fetch_fact/', fetch_fact_view, name='fetch_fact'),
    path('get_fact/', get_fact, name='get_fact')
    
]
