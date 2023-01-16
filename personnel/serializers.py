from rest_framework import serializers
from .models import Department, Personnel


class PersonnelSerializer(serializers.ModelSerializer):
  class Meta:
    model = Personnel
    fields = "__all__"

class DepartmentSerializer(serializers.ModelSerializer):
  personnel = PersonnelSerializer(many = True)
  personnel_count = serializers.SerializerMethodField()  
  class Meta:
    model = Department
    fields = (
      "id",
      "name",
      "personnel_count",
      "personnel"
    )
  def get_personnel_Count(self, obj):
    return obj.personnel.count()

