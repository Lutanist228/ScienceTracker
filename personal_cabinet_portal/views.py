from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def home(request, u_id, u_token):
    return HttpResponse(content=f"Личный кабинет пользователя {u_token}:{u_id}")