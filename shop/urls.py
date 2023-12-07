
from django.urls import path
from .views import *

urlpatterns = [
    path('', index,name='home'),
    path('about',about,name='about'),
    path('product/<int:pk>', product, name='product'),
    path('category/<str:cat>', category, name='category'),
    path('signup/',signup_user, name="signup"),
    path('login/',login_user, name="login"),
    path('logout/',logout_user, name="logout")
]
