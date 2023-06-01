"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from carrepair import views

urlpatterns = [
    path('index', views.index, name = 'index'),
    path('renewpay', views.renewpay, name = 'renewpay'),
    path('reneworder', views.reneworder, name = 'reneworder'),
    path('renewdb', views.renewdb, name = 'renewdb'),
    path('registration', views.registration, name = 'registration'),
    path('order', views.order, name = 'order'),
    path('pay', views.pay, name = 'pay'),
    path('access', views.access, name = 'access'),
    path('postuser', views.postuser, name = 'postuser'),
    path('postregistration', views.postregistration, name = 'postregistration'),
    path('login', views.login, name = 'login'),
    path('', views.login),
]

