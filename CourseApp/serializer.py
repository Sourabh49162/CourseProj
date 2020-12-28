from rest_framework import serializers
from . models import Courses

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ("id", "code", "title", "description")