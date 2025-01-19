from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpRequest, HttpResponse
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User

from utils.additional_functions import retrieve_udata, set_json_value
from config import generate_utoken, read_users
from .serializers import StudentSerializer, SupervisorSerializer
from .models import StudentProfile, SupervisorProfile

class StudentAPI(APIView): 
    def get(self, request: HttpResponse, u_login: str):
        _, udata = retrieve_udata(inputted_information=u_login, json_doc=read_users())
        
        return render(request=request, template_name=r"auth_portal\student_profile_inactive.html", context=udata)
    
    def post(self, request: HttpRequest, u_login: str) -> HttpResponse:
        try:
            request_data = request.POST
            serializer = StudentSerializer(data=request_data)
            
            if serializer.is_valid(raise_exception=True):
                saved_row: StudentProfile = serializer.save()
                set_json_value(user_id=saved_row.pk, url_token=generate_utoken(message=u_login), key_value=u_login, json_doc=read_users())
                _, udata = retrieve_udata(inputted_information=u_login, json_doc=read_users())
                
                return redirect(to=reverse("personal_cabinet_portal", args=(udata["url_token"], udata["user_id"],)))
            else: 
                print("Форма невалидна")
        except KeyError:
            pass
        
        _, udata = retrieve_udata(inputted_information=u_login, json_doc=read_users())    
        
        return render(request=request, template_name=r"auth_portal\student_profile_inactive.html", context=udata)
    
class SupervisorAPI(APIView): 
    def get(self, request: HttpResponse, u_login: str):
        _, udata = retrieve_udata(inputted_information=u_login, json_doc=read_users())
        
        return render(request=request, template_name=r"auth_portal\supervisor_profile_inactive.html", context=udata)
    
    def post(self, request: HttpRequest, u_login: str) -> HttpResponse:
        try:
            request_data = request.POST
            serializer = SupervisorSerializer(data=request_data)
            
            if serializer.is_valid(raise_exception=True):
                saved_row: StudentProfile = serializer.save()
                set_json_value(user_id=saved_row.pk, url_token=generate_utoken(message=u_login), key_value=u_login, json_doc=read_users())
                _, udata = retrieve_udata(inputted_information=u_login, json_doc=read_users())
            
                return redirect(to=reverse("personal_cabinet_portal", args=(udata["url_token"], udata["user_id"],)))
            else:
                print("Форма невалидна")
        except KeyError:
            pass
            
        _, udata = retrieve_udata(inputted_information=u_login, json_doc=read_users())
        
        return render(request=request, template_name=r"auth_portal\supervisor_profile_inactive.html", context=udata)

class AdminAPI(CreateAPIView):
    queryset = User.objects.values("email", "is_staff").all() #!!!!
    
class GeneralApi(APIView):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request=request, template_name=r"auth_layout.html")
    
    def post(self, request: HttpRequest) -> HttpResponse: 
        req_post = request.POST
        error_log = {"error":None}
                
        if req_post['userlogin'] == '' or req_post['userpass'] == '':
            error_log["error"] = "поля формы не заполнены"
            return render(request=request, template_name=r"auth_portal\auth_error.html", context=error_log)
        
        role, _ = retrieve_udata(inputted_information=req_post["userlogin"], json_doc=read_users())

        match role:
            case "STUDENT":
                return redirect(to=reverse(viewname="student_login", args=(req_post['userlogin'],)))
            case "SUPERVISOR":
                return redirect(to=reverse(viewname="supervisor_login", args=(req_post['userlogin'],)))
            case None:
                error_log["error"] = "пользователь не найден в системе"
                return render(request=request, template_name=r"auth_portal\auth_error.html", context=error_log)
            

