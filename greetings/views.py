from django.shortcuts import render
from django.http import HttpResponse

def greetings(request):
    """wyswietla prosty tekst"""
    return HttpResponse("Hello World!")

def personal(request, name):
    """wyswietla personalizowane pozdrowienia"""
    name = name.capitalize()
    return HttpResponse(f"Hello {name}")


