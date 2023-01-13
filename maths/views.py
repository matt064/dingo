from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages


def math(request):
    return render(
        request=request,
        template_name="maths/main.html",
    )

def add(request,a,b):
    a, b = int(a), int(b)
    wynik = a + b
    t = loader.get_template("maths/operation.html")
    c = {"a": a, "b": b, "operacja": "+", "wynik": wynik, "title": "dodawanie"}
    return HttpResponse(t.render(c))


def sub(request,a,b):
    wynik = int(a) - int(b)
    c = {"a":a, "b":b, "operacja": "-", "wynik":wynik}
    return render(
        request=request,
        template_name="maths/main.html",
        context=c
    )

def mul(request,a,b):
    wynik = int(a) * int(b)
    c = {"a":a, "b":b, "operacja": "*", "wynik":wynik}
    return render(
        request=request,
        template_name="maths/main.html",
        context=c
    )


def div(request,a,b):
    a, b = int(a), int(b)
    if b == 0:
        wynik = "Error"
        messages.add_message(request, messages.ERROR, "Dzielenie przez zero!")
    else:
        wynik = a / int(b)
    c = {"a": a, "b": b, "operacja": "/", "wynik": wynik, "title": "dzielenie"}
    return render(
        request=request,
        template_name="maths/operation.html",
        context=c)
    
