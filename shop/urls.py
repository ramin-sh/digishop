
from django.urls import path
from .views import *

urlpatterns = [
    path('', hello,name='home'),
    path('about',about,name='about'),

]
