from django.shortcuts import render,redirect
from .models import Product,Category,Profile
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserCreationForm
from django import forms
from .forms import SignUpform, UpdateUserform, UpdatePasswordForm,UpdateUserInfo
# Create your views here.

def update_info(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id=request.user.id)
        form = UpdateUserInfo(request.POST or None, instance=current_user)

        if form.is_valid():
            form.save()
            
            messages.success(request,'اطلاعات کاربری شما ویرایش شد.')
            return redirect('home')
         
        return render(request, 'update_info.html', {'form':form})
    else:
        messages.success(request,'ابتدا باید لاگین کنید')
        return redirect('home')

def index(request):
    all_products = Product.objects.all()

    return render(request,'index.html',{'products':all_products})

def about(request):

    return render(request=request,template_name='about.html')

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserform(request.POST or None, instance=current_user)

        if user_form.is_valid():
            user_form.save()
            login(request,current_user)
            messages.success(request,'‍پروفایل شما ویرایش شد.')
            return redirect('home')
         
        return render(request, 'update_user.html', {'user_form':user_form})
    else:
        messages.success(request,'ابتدا باید لاگین کنید')
        return redirect('home')
    

def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user

        if request.method == 'POST':
            form = UpdatePasswordForm(current_user, request.POST)
             
            if form.is_valid():
                form.save()
                messages.success(request,'رمز با موفقیت ویرایش شد')
                login(request, current_user)
                return redirect('update_user')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                return redirect('update_password')

        else:
            form = UpdatePasswordForm(current_user)
            return render(request, 'update_password.html', {'form':form} )
    else:
        messages.success(request, 'باید اول لاگین بشی')
        return redirect('home')
    
  

    

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