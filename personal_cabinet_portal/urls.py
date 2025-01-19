from django.urls import path, include
from . import views as v

urlpatterns = [
    path("", v.GeneralApi.as_view(), name="personal_cabinet_portal"),
    path("student_profile/<int:id>", v.StudentProfileViewset.as_view({"get":"process_profile_info", "post":"process_profile_info"}), name="std-profile_actions"),
    path("supervisor_profile/<int:id>", v.SupervisorProfileViewset.as_view({"get":"process_profile_info", "post":"process_profile_info"}), name="sup-back_to_profile"),
]
