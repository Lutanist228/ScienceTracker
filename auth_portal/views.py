from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpRequest, HttpResponse
from django.forms import ValidationError
import os

from utils.additional_functions import retrieve_udata, set_json_value
from config import generate_utoken
from .models import StudentProfile, SupervisorProfile
from config import read_users

class StudentViews():
    def login(request: HttpRequest, u_login: str) -> HttpResponse:
        try:
            if request.POST["POST-status"] == "True":
                request_data = request.POST
                
                stud_row = StudentProfile(group=request_data["group"], faculty=request_data["fac"],
                    speciality=request_data["spec"], education=request_data["educ"],
                    orcid=request_data["orcid"], interest=request_data["interest"])
                
                stud_row.save()
                set_json_value(user_id=stud_row.pk, url_token=generate_utoken(), key_value=u_login, json_doc=read_users())
                _, data = retrieve_udata(inputted_information=u_login, json_doc=read_users())
                
                return redirect(to=reverse("personal_cabinet_portal", args=(data["url_token"], data["user_id"],)))
        except KeyError:
            pass
            
        _, udata = retrieve_udata(inputted_information=u_login, json_doc=read_users())
        
        return render(request=request, template_name=r"auth_portal\student_profile_inactive.html", context=udata)

class SupervisorViews():
    def login(request: HttpRequest, u_login: str) -> HttpResponse:
        try:
            if request.POST["POST-status"] == "True":
                request_data = request.POST
                
                sup_row = SupervisorProfile(profession=request_data["prof"], department=request_data["dep"],
                    orcid=request_data["orcid"], interest=request_data["interest"])
                
                sup_row.save()
                set_json_value(user_id=sup_row.pk, url_token=generate_utoken(), key_value=u_login, json_doc=read_users())
                _, data = retrieve_udata(inputted_information=u_login, json_doc=read_users())
                
                return redirect(to=reverse("personal_cabinet_portal", args=(data["url_token"], data["user_id"],)))
        except KeyError:
            pass
        
        _, udata = retrieve_udata(inputted_information=u_login, json_doc=read_users())
        
        return render(request=request, template_name=r"auth_portal\supervisor_profile_inactive.html", context=udata)

def auth(request: HttpRequest) -> HttpResponse: 
    request_data = request.GET
    error_log = {"error":None}
    
    input_check = list(filter(lambda x: len(x) > 0, request_data.values()))
    
    if len(request_data) != 0:
        if len(input_check) == 0:
            error_log["error"] = "поля формы не заполнены"
            return render(request=request, template_name=r"auth_portal\auth_error.html", context=error_log)
        
        role, _ = retrieve_udata(inputted_information=request_data["userlogin"], json_doc=read_users())

        match role:
            case "STUDENT":
                return redirect(to=reverse("student_login", args=(request_data["userlogin"],)))
            case "SUPERVISOR":
                return redirect(to=reverse("supervisor_login", args=(request_data["userlogin"],)))
            case None:
                error_log["error"] = "пользователь не найден в системе"
                return render(request=request, template_name=r"auth_portal\auth_error.html", context=error_log)
    else:
        return render(request=request, template_name=r"auth_portal\auth_layout.html")

