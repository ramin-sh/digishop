from django.shortcuts import render,redirect
from .models import Product,Category
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages 

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


def category(request,cat):
    cat = cat.replace("-", " ")
    try:
        category = Category.objects.get(name=cat)
        print(cat)
        products = Product.objects.filter(Category=category)
        print(products)
        return render(request,"category.html",{"products":products,"category":category})
    except:
        messages.success(request,"دسته بندی وجود ندارد")
        return  redirect("home")
