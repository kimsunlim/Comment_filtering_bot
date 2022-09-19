from django.urls import path
from filterApp import views

urlpatterns = [
    path('', views.index)
]