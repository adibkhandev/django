from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
   path('',views.home),
   path('reg/',views.reg),
   path('login/',views.login),
   path('products/',views.products),
]
