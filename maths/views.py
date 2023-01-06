from django.shortcuts import render
from django.http import HttpResponse

def math(request):
    return HttpResponse("to bedzie matma")

def add(request,a,b):
    return HttpResponse(int(a) + int(b))

def sub(request,a,b):
    return HttpResponse(int(a) - int(b))

def mul(request,a,b):
    return HttpResponse(int(a) * int(b))

def div(request,a,b):
    if int(b) == 0:
        return HttpResponse("Nie mozna dzielic przez 0")
    else:
        return HttpResponse(int(a) / int(b))
    
