from django.shortcuts import render

def home(request):
    return render(request,'temp/home.html')

def dashboard(request):
    return render(request,'temp/dashboard.html')


def admin_home(request):
    return render(request,'temp/admin.html')

def user_home(request):
    return render(request,'temp/user_home.html')

def driver_home(request):
    return render(request,'temp/driver_home.html')
