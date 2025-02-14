from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True,blank=True)
    shipping_full_name = models.CharField(max_length= 250 )
    shipping_email = models.CharField(max_length=300),
    shipping_address1 = models.CharField(max_length=250, default='',blank=True)
    shipping_address2 = models.CharField(max_length=250, default='',blank=True)
    shipping_city = models.CharField(max_length=25, blank=True)    
    shipping_phone = models.CharField(max_length=25,blank=True)
    shipping_old_cart= models.CharField(max_length=200,blank=True)
    shipping_state = models.CharField(max_length=25,blank=True)
    shipping_zipcode = models.CharField(max_length=25,blank=True)
    shipping_country = models.CharField(max_length=25,blank=True, null=True)

  

    def __str__(self):
        return f'shiping address from {self.shipping_full_name }'


# class  Order(models.Model):
#     user = models.ForeignKey(User, on_delete = models.CASCADE, null=True,blank=True)
#     full_name = models.CharField(max_length= 250 )
#     email = models.EmailField(max_length=300)
#     Shipping_address = models.TextField(max_length=150000)
#     #.........