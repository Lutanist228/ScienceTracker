from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.forms import ValidationError
from dotenv import load_dotenv
import os

from utils.additional_functions import json_reader, retrieve_udata

load_dotenv()

class StudentViews():
    def login(request: HttpRequest, user_data: dict) -> HttpResponse:
        return render(request=request, template_name=r"auth_portal\student_profile.html", context=user_data)

class SupervisorViews():
    def login(request: HttpRequest, user_data: dict) -> HttpResponse:
        return render(request=request, template_name=r"auth_portal\supervisor_profile.html", context=user_data)

def auth(request: HttpRequest) -> HttpResponse: 
    user_data = request.GET
    error_log = {"error":None}
    
    input_check = list(filter(lambda x: len(x) > 0, user_data.values()))
    
    
    
    if len(user_data) != 0:
        if len(input_check) == 0:
            error_log["error"] = "поля формы не заполнены"
            return render(request=request, template_name=r"auth_portal\auth_error.html", context=error_log)
        
        users = json_reader(path=os.environ.get("USERS_PATH"))
        role, data = retrieve_udata(inputted_information=user_data["userlogin"], json_doc=users)

        match role:
            case "STUDENT":
                return StudentViews.login(request=request, user_data=data)
            case "SUPERVISOR":
                return SupervisorViews.login(request=request, user_data=data)
            case None:
                error_log["error"] = "пользователь не найден в системе"
                return render(request=request, template_name=r"auth_portal\auth_error.html", context=error_log)
    else:
        return render(request=request, template_name=r"auth_portal\auth_layout.html")
