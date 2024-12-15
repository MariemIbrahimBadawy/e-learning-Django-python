from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'pages/home.html')

def courses(request):
    return render(request, 'pages/courses.html')

def about(request):
    return render(request, 'pages/about.html')

def login(request):
    path = request.path 
    return render(request , 'pages/page-login.html' , {'path': path})

def register(request):
    path =request.path
    return render(request , 'pages/page-register.html', {'path':path})


