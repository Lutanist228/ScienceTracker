from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def auth(request: HttpRequest): 
    return render(request=request, template_name=r"auth_portal\auth.html")

def login(request: HttpRequest):
    return render(request=request, template_name=r"auth_portal\profile_layout.html")
    