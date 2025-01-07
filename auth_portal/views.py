from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def auth(request: HttpRequest): 
    return render(request=request, template_name="auth_portal\main_layout.html")

def reg(request: HttpRequest):
    return HttpResponse("Страница регистрации")
    