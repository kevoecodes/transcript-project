

from app.models import Lecturer
from rest_framework import serializers


class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = "__all__"
