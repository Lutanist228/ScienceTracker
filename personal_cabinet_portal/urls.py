from django.urls import path, include
from . import views as v

urlpatterns = [
    path("", v.GeneralApi.as_view(), name="personal_cabinet_portal"),
    path("student_profile/<int:id>", v.StudentProfileViewset.as_view({"get":"display_profile_info"}), name="std-back_to_profile"),
    path("student_profile/<int:id>", v.StudentProfileViewset.as_view({"put":"update_profile_info"}), name="std-update_profile"),
    path("supervisor_profile/<int:id>", v.SupervisorProfileViewset.as_view({"get":"get_profile_info"}), name="sup-back_to_profile"),
]
