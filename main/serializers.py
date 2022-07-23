from msilib.schema import Class
from rest_framework import serializers
from .models import Farmer,Crop,Fertilizer,Farm,Schedule

'''
Serializer for Farmer model
'''
class CropSerializer(serializers.ModelSerializer):
  class Meta:
    model = Crop
    fields = '__all__'


class FarmerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Farmer
    fields = '__all__'


class FertilizerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Fertilizer
    fields = '__all__'

  
class FarmSerializer(serializers.ModelSerializer):
  class Meta:
    model = Farm
    fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Schedule
    fields = '__all__'
    
