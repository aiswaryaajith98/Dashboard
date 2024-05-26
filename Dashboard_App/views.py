from django.shortcuts import render

def dashboard(request):
    return render(request,'index.html')

def users(request):
    return render(request,'users-profile.html')

