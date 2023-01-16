from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DepartmentSerializer, PersonnelSerializer
from .models import Department, Personnel
from rest_framework import generics

# Create your views here.

# class DepartmentView(viewsets.ModelViewSet):
#   queryset = Department.objects.all()
#   serializer_class = DepartmentSerializer


# class PersonnelView(viewsets.ModelViewSet):
#   queryset = Personnel.objects.all()
#   serializer_class = PersonnelSerializer

class DepartmentView(generics.ListCreateAPIView):
  serializer_class = DepartmentSerializer
  queryset = Department.objects.all()