from rest_framework import serializers
from .models import Department, Personnel




class PersonnelSerializer(serializers.ModelSerializer):
  class Meta:
    model = Personnel
    fields = "__all__"

class DepartmentSerializer(serializers.ModelSerializer):
  personnel = PersonnelSerializer(many = True)
  class Meta:
    model = Department
    fields = (
      "id",
      "name",
      "personnel_count",
      "personnel"
    )

