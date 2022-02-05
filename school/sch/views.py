from django.shortcuts import render
from rest_framework import viewsets
from ..models import School
from .serializers import SchoolSerializer


# Create your views here.
class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all().order_by('school_name')
    serializer_class = SchoolSerializer
