from django.urls import path, include
from . import views as v

urlpatterns = [
    path("", v.auth, name="authorization"),
    path("student_profile:<str:u_login>/", v.StudentViews.login, name="student_login"),
    path("supervisor_profile:<str:u_login>/", v.SupervisorViews.login, name="supervisor_login"),
    path("<str:u_role>/<str:u_token>№<int:u_id>/", include("personal_cabinet_portal.urls"), name="personal_cabinet_portal"),
]
