from django.shortcuts import render
from django.http import HttpResponse

def greetings(request):
    """wyswietla prosty tekst"""
    return render(
        request=request,
        template_name="greetings/hello.html",
    )

def about(request):
    """wyswietla informacje o autorze"""
    c = {"imie": "Jan", "nazwisko": "Nowak"}
    return render(
        request=request,
        template_name = "greetings/about.html",
        context=c,
    )

def contact(request):
    email = "janek@examole.com"
    tel = 481112223
    c = {"email": email, "tel": tel}
    return render(
        request=request,
        template_name="greetings/contact.html",
        context=c
    )


