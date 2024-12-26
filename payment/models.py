from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True,blank=True)
    full_name = models.CharField(max_length= 250 )
    email = models.CharField(max_length=300),
    address1 = models.CharField(max_length=250, default='',blank=True)
    address2 = models.CharField(max_length=250, default='',blank=True)
    city = models.CharField(max_length=25, blank=True)    
    phone = models.CharField(max_length=25,blank=True)
    old_cart= models.CharField(max_length=200,blank=True)
    state = models.CharField(max_length=25,blank=True)
    zipcode = models.CharField(max_length=25,blank=True)
    country = models.CharField(max_length=25,blank=True, null=True)

  

    def __str__(self):
        return f'shiping address from {self.full_name}'
