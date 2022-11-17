from django.contrib import admin
from django.urls import path
from todoapp import views

urlpatterns = [
    path('',views.index),
    path('home',views.home),
    path('edit/<rid>',views.edit),
    path('delete/<rid>',views.delete),
    path('dashboard',views.dashboard)
]
