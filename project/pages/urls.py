from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name ='index'),
    path('home', views.home, name ='home'),
    path('courses', views.courses, name ='courses'),
    path('about', views.about, name ='about'),
    path('login', views.login, name ='login'),
    path('register', views.register, name ='register'),
    # path('about', views.about, name ='about')
]