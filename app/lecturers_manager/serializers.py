

from app.models import Lecturer, StudentModuleResult, ResultsAssignment
from rest_framework import serializers


class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = "__all__"


class StudentModuleResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModuleResult
        fields = "__all__"


class ResultsAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultsAssignment
        fields = "__all__"



