from django.shortcuts import render
from .models import Product
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    all_products = Product.objects.all()

    return render(request,'index.html',{'products':all_products})

def about(request):

    return render(request=request,template_name='about.html')

def product(request,pk):
    product = Product.objects.get(id=pk)
    context = {'product':product}
    return render(request=request,template_name='product.html', context=context)

