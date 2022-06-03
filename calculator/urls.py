from django.urls import path,include
from django.contrib import admin
from calculator import views

urlpatterns=[
    path("home",views.HomeView.as_view()),
    path("add",views.AddView.as_view()),
]