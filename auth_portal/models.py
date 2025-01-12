from django.db import models

class StudentProfile(models.Model): 
    group = models.CharField(max_length=255)
    faculty = models.CharField(max_length=255)
    speciality = models.CharField(max_length=510)
    education = models.CharField(max_length=255)
    orcid = models.CharField(max_length=255, blank=True)
    interest = models.CharField(max_length=510, blank=True)
    
class SupervisorProfile(models.Model): 
    profession = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    orcid = models.CharField(max_length=255, blank=True)
    interest = models.CharField(max_length=510, blank=True)
    