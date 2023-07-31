from django.shortcuts import render

# Create your views here.

def data(request):
    d={'name':'SEENU','age':21,'mno':9090879080}
    return render(request,'data.html',context=d)

def new(request):
    dic={'a':10,'b':20,'c':30}
    return render(request,'new.html',context=dic)