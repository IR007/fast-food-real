# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('payments/add/', views.add_payment, name='add_payment'),
]
