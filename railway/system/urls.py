from django.contrib import admin
from django.urls import path
from system import views

urlpatterns = [
    path("", views.home, name='system'),
    path("homebtn.html", views.homebtn, name='homebtn'),
    path("contact", views.contact, name='contact'), 
    path("index.html", views.index, name='index'),
    path("index1.html", views.index1, name='index1'),
]