from django.urls import path, include, re_path
from . import views as v
from dotenv import load_dotenv
import os

load_dotenv()

urlpatterns = [
    path("", v.GeneralApi.as_view(), name="authorization"),
    path("student_profile:<str:u_login>/", v.StudentAPI.as_view(), name="student_login"),
    path("supervisor_profile:<str:u_login>/", v.SupervisorAPI.as_view(), name="supervisor_login"),
    path(f"api/{os.environ.get("API_PATH_URL")}/student/", v.StudentAPI.as_view(), name="student_api"),
    path(f"api/{os.environ.get("API_PATH_URL")}/supervisor/", v.SupervisorAPI.as_view(), name="supervisor_api"),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path("<str:u_token>№<int:u_id>/", include("personal_cabinet_portal.urls")),
]
