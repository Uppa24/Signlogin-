from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login_fun(request):
    if request.method=='POST':
        name = request.POST['txtname']
        password = request.POST['txtpassword']
        user = authenticate(username=name,password=password)
        if user is not None:
            if user.is_superuser:
                return  HttpResponse(f"<h1>successfully loged in</h1>")
            else:
                return render(request,'login.html',{"msg":True})
        else:
            return render(request,'login.html',{"msg":True})
    else:
        return render(request,'login.html',{"msg":False})


def signup_fun(request):
    if request.method=='POST':
        name=request.POST['txtname']
        email=request.POST['txtemail']
        password=request.POST['txtpassword']
        if User.objects.filter(Q(username=name)|Q(email=email)|Q(password=password)).exists():
            return render(request,'signup.html',{"msg":True})
        else:
            u1=User.objects.create_superuser(username=name,email=email,password=password)
            u1.save()
            return render(request,'login.html')
    return render(request,'signup.html',{"msg":False})