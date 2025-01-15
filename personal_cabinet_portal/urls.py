from django.urls import path, include
from . import views as v

urlpatterns = [
    path("", v.home, name="personal_cabinet_portal"),
    path("profile/", v.StudentViews.profile, name="back_to_profile"),
]
