from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

class StudentViews():
    def profile(request):
        return render(request=request, template_name=r"personal_cabinet_portal\student_profile_active.html")

def home(request, u_id, u_token):
    return HttpResponse(content=f"Личный кабинет пользователя {u_token}:{u_id}")

