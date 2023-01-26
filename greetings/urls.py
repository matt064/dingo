from django.urls import path
from greetings.views import greetings, about, contact


app_name = "greetings"
urlpatterns = [
    path('', greetings, name='greetings'),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
]