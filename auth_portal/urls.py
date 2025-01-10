from django.urls import path
from . import views as v

urlpatterns = [
    path("", v.auth, name="authorization"),
    path("student_profile/", v.StudentViews.login, name="sup_login"),
    path("supervisor_profile/", v.StudentViews.login, name="sup_login")
]
