from django.urls import path
from . import views as v

urlpatterns = [
    path("", v.auth, name="authorization"),
    path("home/", v.home, name="cabinet"),
]
