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

class EmployeeListView(View):
    def get(self,request,*args,**kwargs):
        qs=Employee.objects.all()
        return render(request,"emp-list.html",{"employees":qs})

class EmployeeDetailView(View):
    def get(self,request,*args,**kwargs):
        #kwargs={emp_id:emp_100}
        qs=Employee.objects.get(eid=kwargs.get("emp_id"))
        return render(request,"emp-detail.html",{"employee":qs})

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

class EmployeeDeleteView(View):
    def get(self,request,*args,**kwargs):
        eid=kwargs.get("emp_id")
        employee=Employee.objects.get(eid=eid)
        employee.delete()
        messages.success(request, "employee deleted successfully")
        return redirect("emp-list")

def index(request):
    return render(request,"base.html")





