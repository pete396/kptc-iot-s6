from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from . models import *
from django.db import IntegrityError
from django.conf import settings
from django.contrib import messages

def public(request):
    return render(request,'public.html')

def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            usr = User.objects.get(name=name) 
            alert = "<script>alert('Name already exists'); window.location.href='/register/';</script>"
            return HttpResponse(alert)
        except User.DoesNotExist:  
        
            new_user = User(name=name, phone_number=phone_number, email=email, password=password)
            new_user.save()
            return redirect('login')
    return render(request, 'register.html')



def login(request):
    if request.method == 'POST':
      name=request.POST.get('name')
      password=request.POST.get('password')
      try:
        usr=User.objects.get(name=name,password=password)
        if usr:
            request.session['id']=usr.id 
            request.session['name'] = usr.name
            return redirect('index')
      except:
            alert="<script>alert('invalid credentials'); window.location.href='/login/';</script>"
            return HttpResponse(alert)
      return redirect('public')
    return render(request,'login.html') 



def logout(request):
    request.session.flush()
    return redirect('public')


def profile(request):
    name=request.session.get('name')
    if name is not None:
        try:
            user=User.objects.get(name=name)
            return render(request,'profile.html',{'user':user})
        except User.DoesNotExist:
            messages.error(request,'user not found!!!!')
            return redirect('login')
    else:
        return redirect('login')
    
def editprofile(request):
    name = request.session.get('name')
    user = User.objects.get(name=name)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        user.name = name
        user.email = email
        user.save()
        messages.success(request, 'Profile Updated successfully!')
        return redirect('profile')
    return render(request, 'editprofile.html', {'user': user})


def admin_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        aemail="admin@gmail.com"
        apass="123"
        if email == aemail:
            if password == apass:
                return redirect('admin_home')
            
    else:
        return render(request,'admin_login.html')
    
def admin_home(request):
    return render(request,'admin_home.html')


def user_list(request):
    user = User.objects.all()
    return render(request,'user_list.html',{'user':user})



