from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpRequest, HttpResponse
from django.forms import ValidationError
import os

from utils.additional_functions import json_reader, retrieve_udata
from config import USERS

class StudentViews():
    def login(request: HttpRequest, u_login: str) -> HttpResponse:
        _, udata = retrieve_udata(inputted_information=u_login, json_doc=USERS)
        
        return render(request=request, template_name=r"auth_portal\student_profile_inactive.html", context=udata)

class SupervisorViews():
    def login(request: HttpRequest, u_login: str) -> HttpResponse:
        _, udata = retrieve_udata(inputted_information=u_login, json_doc=USERS)
        
        return render(request=request, template_name=r"auth_portal\supervisor_profile_inactive.html", context=udata)

def auth(request: HttpRequest) -> HttpResponse: 
    user_data = request.GET
    error_log = {"error":None}
    
    input_check = list(filter(lambda x: len(x) > 0, user_data.values()))
    
    if len(user_data) != 0:
        if len(input_check) == 0:
            error_log["error"] = "поля формы не заполнены"
            return render(request=request, template_name=r"auth_portal\auth_error.html", context=error_log)
        
        role, _ = retrieve_udata(inputted_information=user_data["userlogin"], json_doc=USERS)

        match role:
            case "STUDENT":
                return redirect(to=reverse("student_login", args=(user_data["userlogin"], )))
            case "SUPERVISOR":
                return redirect(to=reverse("supervisor_login", args=(user_data["userlogin"], )))
            case None:
                error_log["error"] = "пользователь не найден в системе"
                return render(request=request, template_name=r"auth_portal\auth_error.html", context=error_log)
    else:
        return render(request=request, template_name=r"auth_portal\auth_layout.html")

