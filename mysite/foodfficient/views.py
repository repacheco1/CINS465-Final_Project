from django.shortcuts import render
from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('Hello, World! This is the beggining for foodfficient!')
# Create your views here.
