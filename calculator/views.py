import math

from django.shortcuts import render
from django.views.generic import View

class HomeView(View):
    def get(self,request):
        return render(request,"calc-home.html")

class AddView(View):
    def get(self,request):
        return render(request,"add.html")
    def post(self,request):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)+int(n2)
        # print(result)
        return render(request, "add.html",{"res":result})

class SubView(View):
    def get(self,request):
        return render(request,"sub.html")
    def post(self,request):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)-int(n2)
        # print(result)
        return render(request, "sub.html",{"res":result})

class DivView(View):
    def get(self,request):
        return render(request,"div.html")
    def post(self,request):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)/int(n2)
        # print(result)
        return render(request, "div.html",{"res":result})

class FactView(View):
    def get(self,request):
        return render(request,"fact.html")
    def post(self,request):
        n1=request.POST.get("num1")
        result=math.factorial(int(n1))
        # print(result)
        return render(request, "fact.html",{"res":result})
