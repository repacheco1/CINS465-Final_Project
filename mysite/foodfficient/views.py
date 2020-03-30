from django.shortcuts import render
from django.http import HttpResponse

def homePageView(request):
    context = {
        "title":"Foodfficient",
        "pageTitle":"Welcome to Foodfficient!",
        "body":"",
        "body2":"",
    }
    return render(request, "index.html", context=context)
# Create your views here.
