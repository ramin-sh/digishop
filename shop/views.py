from django.shortcuts import render,redirect
from .models import Product,Category
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserCreationForm
from django import forms
from .forms import SignUpform
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

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"با موفقیت وارد شدید")
            return redirect("home")
        else:
            messages.success(request,"نام کاربری یا کلمه عبور اشتباه است")
            return redirect("login")
    
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    messages.success(request,"با موفقیت خارج شدید")
    return redirect("home")



def signup_user(request):

    form = SignUpform()
    if request.method == "POST":
        form = SignUpform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            user = authenticate(request,username=username,password=password1)
            messages.success(request,('حساب کاربری شما ساخته شد'))
            login(request=request,user=user)
            return redirect("home")
        
        else:
            messages.success(request,('ثبت نام شما با مشکل مواجه شد'))
            return redirect("signup")
    else:

        return render(request,'signup.html',{'form':form})