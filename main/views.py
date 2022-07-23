from django.shortcuts import render
from rest_framework import  viewsets 
from .serializers import CropSerializer, FarmerSerializer,FarmSerializer, FertilizerSerializer, ScheduleSerializer
from .models import Crop, Farmer,Farm, Fertilizer, Schedule
from django.http import HttpRequest


class FarmerViewSet(viewsets.ModelViewSet):
  queryset = Farmer.objects.all()
  serializer_class = FarmerSerializer

class FarmViewSet(viewsets.ModelViewSet):
  queryset = Farm.objects.all()
  serializer_class = FarmSerializer

class CropViewSet(viewsets.ModelViewSet):
  queryset = Crop.objects.all()
  serializer_class = CropSerializer

class FertilizerViewSet(viewsets.ModelViewSet):
  queryset = Fertilizer.objects.all()
  serializer_class = FertilizerSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
  queryset = Schedule.objects.all()
  serializer_class = ScheduleSerializer

def index(request: HttpRequest):
  return render(request,'main/home.html')