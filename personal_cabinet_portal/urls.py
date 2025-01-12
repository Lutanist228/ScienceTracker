from django.urls import path
from . import views as v

urlpatterns = [
    path("", v.home, name="personal_cabinet_portal"),
]
