# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from django.views.generic import View
# from employee.forms import EmployeeForm
# from django.contrib import messages
# # Create your views here.
# #function based views
# #class based views
#
#
# # def index(request):
# #     return render(request,"home.html")
# #
# # def login(request):
# #     return render(request,"login.html")
# #
# # def logout(request):
# #     return render(request,"logout.html")
#
# class LoginView(View):
#     def get(self,request):
#         form = RegistrationForm()
#         return render(request, "login.html", {"form": form})
#     def post(self,request):
#         print(request.POST.get("user"))
#         print(request.POST.get("pword"))
#         return render(request, "login.html")
#
# class IndexView(View):
#     def get(self,request):
#         return render(request,"home.html")
#     def post(self,request):
#         print(request.POST.get("fname"))
#         print(request.POST.get("lname"))
#         print(request.POST.get("user_id"))
#         print(request.POST.get("pword"))
#         return render(request,"home.html")
#
#
# class LogoutView(View):
#     def get(self,request):
#         return render(request,"logout.html")
#
# class EmployeeCreaetView(View):
#     form_class=EmployeeForm
#     template_name="add-emp.html"
#     def get(self,request):
#         form=self.form_class
#         return render(request,self.template_name,{"form":form})
#     def post(self,request):
#         form=self.form_class(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data.get("eid"))
#             print(form.cleaned_data.get("employee_name"))
#             print(form.cleaned_data.get("Email"))
#             messages.success(request,"Successfully added")
#             return redirect("add-emp")
#         else:
#             messages.error(request,"Profile not added")
#             return render(request,self.template_name,{"form":form})
from django.views.generic import View
from employee.forms import EmployeeCreateForm
from django.shortcuts import render,redirect
from django.contrib import messages
from employee.models import Employee
from employee.forms import UserRegistrationForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator

def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            messages.error(request,"You must login")
            return redirect("sign-in")
    return wrapper

@method_decorator(signin_required,name="dispatch")
class EmployeeCreateView(View):
    form_class=EmployeeCreateForm
    def get(self,request,*args,**kwargs):
        return render(request,"add-emp.html",{"form":self.form_class()})
    def post(self,request,*args,**kwargs):
        form=EmployeeCreateForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            # Employee.objects.create(
            #     eid=form.cleaned_data.get("eid"),
            #     employee_name=form.cleaned_data.get("employee_name"),
            #     designation=form.cleaned_data.get("designation"),
            #     salary=form.cleaned_data.get("salary"),
            #     email=form.cleaned_data.get("email"),
            #     experience=form.cleaned_data.get("experience"),
            # )
            #
            messages.success(request,"employee added successfully")
            return redirect("add-emp")
        else:
            messages.error(request, "employee added unsuccessfully")
            return render(request, "add-emp.html", {"form": self.form_class()})

@method_decorator(signin_required,name="dispatch")
class EmployeeListView(View):
    def get(self,request,*args,**kwargs):
        qs=Employee.objects.all()
        return render(request,"emp-list.html",{"employees":qs})

@method_decorator(signin_required,name="dispatch")
class EmployeeDetailView(View):
    def get(self,request,*args,**kwargs):
        #kwargs={emp_id:emp_100}
        qs=Employee.objects.get(eid=kwargs.get("emp_id"))
        return render(request,"emp-detail.html",{"employee":qs})

@method_decorator(signin_required,name="dispatch")
class EmployeeEditView(View):
    def get(self,request,*args,**kwargs):
        eid=kwargs.get("emp_id")
        employee=Employee.objects.get(eid=eid)
        form=EmployeeCreateForm(instance=employee)
        return render(request,"emp-edit.html",{"form":form})
    def post(self,request,*args,**kwargs):
        eid = kwargs.get("emp_id")
        employee = Employee.objects.get(eid=eid)
        form = EmployeeCreateForm(request.POST, instance=employee, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "employee edited successfully")
            return redirect("add-emp")
        else:
            messages.error(request, "employee edited unsuccessfully")
            return render(request, "add-emp.html", {"form": form})

@method_decorator(signin_required,name="dispatch")
class EmployeeDeleteView(View):
    def get(self,request,*args,**kwargs):
        eid=kwargs.get("emp_id")
        employee=Employee.objects.get(eid=eid)
        employee.delete()
        messages.success(request, "employee deleted successfully")
        return redirect("emp-list")

@signin_required
def index(request):
    return render(request,"base.html")

class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=UserRegistrationForm()
        return render(request,"registration.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your account has been created")
            return redirect("sign-up")
        else:
            messages.error(request,"account creation failed")
            return render(request,"registration.html",{"form":form})

class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(username=uname,password=pwd)
            if user:
                # print("success")
                login(request,user)
                return redirect("emp-list")
            else:
                return render(request,"login.html",{"form":form})

@signin_required
def sign_out(request,*args,**kwargs):
    logout(request)
    return redirect("sign-in")

