from msilib.schema import Class
from tokenize import Name
from rest_framework import serializers
from .models import Farmer,Crop,Fertilizer,Farm,Schedule

'''
Serializer for Farmer model
'''

class CropSerializer(serializers.ModelSerializer):
  class Meta:
    model = Crop
    fields = ['id','name']

class FarmSerializer(serializers.ModelSerializer):
  class Meta:
    model = Farm
    fields = ['id','area','village','crop_id','farmer_id','sowing_date']

class FarmerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Farmer
    fields = ['id','name','phone_number','language']


class FertilizerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Fertilizer
    fields = ['id','name','price_per_unit','quantity_unit']

  
class ScheduleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Schedule
    fields = ['id','farm','fertilizer','quantity']

class FarmWithFarmerSerializer(serializers.Serializer):
  farmer = FarmerSerializer()
  crop = CropSerializer()
  id = serializers.UUIDField()
  village = serializers.CharField()
  area = serializers.CharField()
  class Meta:
    fields = '__all__'

class ScheduleWithFarmAndFertilizer(serializers.Serializer):
  farm = FarmSerializer()
  fertilizer = FertilizerSerializer()
  id = serializers.UUIDField()
  quantity = serializers.FloatField()
  days_after_sowing = serializers.IntegerField()
  class Meta:
    fields = '__all__'