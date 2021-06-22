"""MegaProject URL Configuration

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
from django.urls import path
from . import views

app_name = 'T_kart'
urlpatterns = [
    path('', views.index.as_view(), name="T-kart-Home"),
    path('product-<slug:slug>/', views.productView.as_view(), name="product-view"),
    path('kart/', views.kart.as_view(), name="kart"),
    path('checkout/', views.checkout.as_view(), name="checkout"),
    path('signUp/', views.Signup.as_view(), name="signUp"),
    path('login/', views.Login.as_view(), name="login"),
    path('logout/', views.logout , name='logout'),
    path('my-account/', views.myAccount.as_view(), name="myAccount"),
    path('wishlist/', views.wishlist.as_view(), name="wishlist"),
    path('compare/', views.compare.as_view(), name="compare"),

]
