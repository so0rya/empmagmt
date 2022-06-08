from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from employee.forms import EmployeeForm
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
        form = RegistrationForm()
        return render(request, "login.html", {"form": form})
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

class EmployeeCreaetView(View):
    form_class=EmployeeForm
    template_name="add-emp.html"
    def get(self,request):
        form=self.form_class
        return render(request,self.template_name,{"form":form})
    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            print(form.cleaned_data.get("eid"))
            print(form.cleaned_data.get("employee_name"))
            print(form.cleaned_data.get("Email"))
            return render(request,self.template_name,{"form":form})
        else:
            return render(request,self.template_name,{"form":form})