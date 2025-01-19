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
    
    @action(detail=True, methods=["get", "post"])
    def process_profile_info(self, request: HttpRequest, u_token: str, id: int):
        def load_data(return_partial: bool = False) -> dict:
            _, u_data = retrieve_udata(inputted_information=u_token, json_doc=read_users())
            profile_data = self.get_object()
            
            if return_partial == False:
                profile_data = {"group":profile_data.group, "faculty":profile_data.faculty, "speciality":profile_data.speciality, "education":profile_data.education, 
                                    "orcid":profile_data.orcid, "interest":profile_data.interest, **u_data}
                return profile_data
            else:
                profile_data = {"group":profile_data.group, "faculty":profile_data.faculty, "speciality":profile_data.speciality, "education":profile_data.education, 
                                    "orcid":profile_data.orcid, "interest":profile_data.interest}
                return profile_data, u_data
            
        if request.method == 'GET':
            return render(request=request, template_name=r"personal_cabinet_portal\student_profile_active.html", context={**load_data()})
        elif request.method == 'POST':
            partial_data = load_data(return_partial=True)
            
            serializer: StudentSerializer = self.get_serializer(self.get_object(), data=request.data, partial=True)
            
            if serializer.is_valid():
                serializer.save()
                return render(request=request, template_name=r"personal_cabinet_portal\student_profile_active.html", context={**load_data()})
            else:
                return render(request=request, template_name=r"personal_cabinet_portal\student_profile_active.html", context={**partial_data[0], **partial_data[1]})
    
class SupervisorProfileViewset(ModelViewSet):
    queryset = SupervisorProfile.objects.all()
    serializer_class = SupervisorSerializer
    lookup_field = 'id'
    
    @action(detail=True, methods=["get", "post"])
    def process_profile_info(self, request: HttpRequest, u_token: str, id: int):
        def load_data(return_partial: bool = False) -> dict:
            _, u_data = retrieve_udata(inputted_information=u_token, json_doc=read_users())
            profile_data = self.get_object()
            
            if return_partial == False:
                profile_data = {"profession":profile_data.profession, "department":profile_data.department, "orcid":profile_data.orcid, 
                                "interest":profile_data.interest, **u_data}
                return profile_data
            else:
                profile_data = {"profession":profile_data.profession, "department":profile_data.department, "orcid":profile_data.orcid, 
                                "interest":profile_data.interest}
                return profile_data, u_data

        if request.method == 'GET':
            return render(request=request, template_name=r"personal_cabinet_portal\supervisor_profile_active.html", context={**load_data()})
        elif request.method == 'POST':
            partial_data = load_data(return_partial=True)
            
            serializer: SupervisorSerializer = self.get_serializer(self.get_object(), data=request.data, partial=True)
            
            if serializer.is_valid():
                serializer.save()
                return render(request=request, template_name=r"personal_cabinet_portal\supervisor_profile_active.html", context={**load_data()})
            else:
                return render(request=request, template_name=r"personal_cabinet_portal\supervisor_profile_active.html", context={**partial_data[0], **partial_data[1]})
        
class GeneralApi(APIView):
    def get(self, request: HttpRequest, u_token):
        role, u_data = retrieve_udata(inputted_information=u_token, json_doc=read_users())
        
        match role:
            case "STUDENT":
                return render(request=request, template_name=r"personal_cabinet_portal\student_cabinet.html", context={"profile":f"student_profile/{u_data["user_id"]}"})
            case "SUPERVISOR":
                return render(request=request, template_name=r"personal_cabinet_portal\supervisor_cabinet.html", context={"profile":f"supervisor_profile/{u_data["user_id"]}"})
        
