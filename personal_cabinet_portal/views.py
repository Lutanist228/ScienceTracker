from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpRequest
from rest_framework.decorators import action

from config import read_users
from utils.additional_functions import retrieve_udata
from auth_portal.models import StudentProfile, SupervisorProfile
from auth_portal.serializers import StudentSerializer, SupervisorSerializer
from rest_framework.viewsets import ModelViewSet


class StudentProfileViewset(ModelViewSet):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'
    profile_data = None
    
    @action(detail=True, methods=['get'])
    def display_profile_info(self, request: HttpRequest, u_token: str, id: int):
        _, u_data = retrieve_udata(inputted_information=u_token, json_doc=read_users())
        
        profile_data = self.get_object()
        self.profile_data = {"group":profile_data.group, "faculty":profile_data.faculty, "speciality":profile_data.speciality, "education":profile_data.education, 
                             "orcid":profile_data.orcid, "interest":profile_data.interest, **u_data}
                
        return render(request=request, template_name=r"personal_cabinet_portal\student_profile_active.html", context={**self.profile_data})
    
    @action(detail=True, methods=["put"])
    def update_profile_info(self, request: HttpRequest, u_token: str, id: int):
        pass
    
class SupervisorProfileViewset(ModelViewSet):
    queryset = SupervisorProfile.objects.all()
    serializer_class = SupervisorSerializer
    lookup_field = 'id'
    profile_data = None
    
    @action(detail=True, methods=['get'])
    def get_profile_info(self, request: HttpRequest, u_token: str, id: int):
        _, u_data = retrieve_udata(inputted_information=u_token, json_doc=read_users())
        
        profile_data = self.get_object()
        self.profile_data = {"profession":profile_data.profession, "department":profile_data.department, "orcid":profile_data.orcid, "interest":profile_data.interest, **u_data}
                
        return render(request=request, template_name=r"personal_cabinet_portal\supervisor_profile_active.html", context={**self.profile_data})
    
class GeneralApi(APIView):
    def get(self, request: HttpRequest, u_token):
        return render(request=request, template_name=r"personal_cabinet.html")

