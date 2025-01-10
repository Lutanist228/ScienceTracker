from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from dotenv import load_dotenv
import os

from utils.additional_functions import json_reader, retrieve_urole

load_dotenv()

class StudentViews():
    def login(request: HttpRequest):
        return render(request=request, template_name=r"auth_portal\student_profile.html")

class SupervisorViews():
    def login(request: HttpRequest):
        return render(request=request, template_name=r"auth_portal\supervisor_profile.html")

def auth(request: HttpRequest): 
    users = json_reader(path=os.environ.get("USERS_PATH"))
    role = retrieve_urole(inputted_information="samokhin_a_s@student.sechenov.ru", json_doc=users)
    
    match role:
        case "STUDENT":
            acc_url = "student_profile/"
        case "SUPERVISOR":
            acc_url = "supervisor_profile/"
    
    return render(request=request, template_name=r"auth_portal\auth.html", context={"url":acc_url})


    