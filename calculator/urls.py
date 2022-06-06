from django.urls import path,include
from django.contrib import admin
from calculator import views

urlpatterns=[
    path("home",views.HomeView.as_view(),name="calchome"),
    path("add",views.AddView.as_view(),name="calc-add"),
    path("sub", views.SubView.as_view(),name="calc-sub"),
    path("div", views.DivView.as_view(),name="calc-div"),
    path("fact",views.FactView.as_view(),name="calc-fact"),
    path("wordcount",views.WordCount.as_view(),name="calc-wcount"),
    path("prime",views.PrimeNum.as_view(),name="calc-prime")
]