from django.urls import path
from . import views as v

urlpatterns = [
    path("", v.auth, name="authorization"),
    path("reg/", v.reg, name="registration")
]
