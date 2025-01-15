from rest_framework import serializers
from .models import StudentProfile, SupervisorProfile

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = "__all__"

    def create(self, validated_data):
        return StudentProfile.objects.create(**validated_data)

class SupervisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupervisorProfile
        fields = "__all__"

    def create(self, validated_data):
        return SupervisorProfile.objects.create(**validated_data)