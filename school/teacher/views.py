from django.shortcuts import render
from rest_framework import viewsets
from ..models import Teacher
from .serializers import TeacherSerializer


# Create your views here.
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all().order_by('first_name')
    serializer_class = TeacherSerializer
