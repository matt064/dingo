from django.urls import path
from greetings.views import greetings, personal

urlpatterns = [
    path('', greetings),
    path("<name>", personal),
]