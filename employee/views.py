from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
# Create your views here.
#function based views
#class based views


# def index(request):
#     return render(request,"home.html")
#
# def login(request):
#     return render(request,"login.html")
#
# def logout(request):
#     return render(request,"logout.html")

class LoginView(View):
    def get(self,request):
        return render(request,"login.html")
    def post(self,request):
        print(request.POST.get("user"))
        print(request.POST.get("pword"))
        return render(request, "login.html")

class IndexView(View):
    def get(self,request):
        return render(request,"home.html")
    def post(self,request):
        print(request.POST.get("fname"))
        print(request.POST.get("lname"))
        print(request.POST.get("user_id"))
        print(request.POST.get("pword"))
        return render(request,"home.html")


class LogoutView(View):
    def get(self,request):
        return render(request,"logout.html")