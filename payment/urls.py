
from django.urls import path
from .views import *

urlpatterns = [
    path('payment_success/', payment_success,name='payment_sucess'),
]