import math
from calculator.forms import OperationForm

from django.shortcuts import render
from django.views.generic import View

class HomeView(View):
    def get(self,request):
        return render(request,"calc-home.html")

class AddView(View):
    def get(self,request):
        form=OperationForm()
        return render(request,"add.html",{"form":form})
    def post(self,request):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)+int(n2)
        # print(result)
        return render(request, "add.html",{"res":result})

class SubView(View):
    def get(self,request):
        form = OperationForm()
        return render(request,"sub.html", {"form": form})
    def post(self,request):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)-int(n2)
        # print(result)
        return render(request, "sub.html",{"res":result})

class DivView(View):
    def get(self,request):
        form = OperationForm()
        return render(request, "div.html", {"form": form})
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

class WordCount(View):
    def get(self,request):
        return render(request,"wordcount.html")
    def post(self,request):
        word=request.POST.get("word")
        wordcount=word.split(" ")
        wc={}
        for w in wordcount:
            if w not in wc:
                wc[w]=1
            else:
                wc[w]+=1

        return render(request,"wordcount.html",{"wordcounts":wc})

class PrimeNum(View):
    def get(self, request):
        return render(request, "primenumber.html")
    def post(self,request):
        a=int(request.POST.get("num1"))
        b=int(request.POST.get("num2"))
        count=[]
        for i in range(a,b+1):
            for j in range(2,i):
                if(i%j==0):
                    break
                else:
                    count.append(i)
        return render(request, "primenumber.html",{"result":count})


