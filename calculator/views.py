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


