from django.http import HttpResponse
from django.shortcuts import render


def set_session(request):
   request.session['sname'] = 'Django'
   request.session['semail'] = 'django@reinhard.com'
   return HttpResponse("session is set")

def get_session(request):
   student_name = request.session['sname']
   student_email = request.session['semail']
   return HttpResponse(student_name+" "+student_email)