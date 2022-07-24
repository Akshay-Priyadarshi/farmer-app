from datetime import timedelta
from django.utils import timezone
from django.shortcuts import render
from rest_framework import  viewsets
from main import serializers

from main.serializers import CropSerializer, FarmSerializer, FarmWithFarmerSerializer, FarmerSerializer, FertilizerSerializer, ScheduleSerializer, ScheduleWithFarmAndFertilizer 
from .models import Crop, Farmer,Farm, Fertilizer, Schedule
from django.http import HttpRequest
from django.db.models import F,Sum


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



def farmerswithcrops(request: HttpRequest):
  context = {}
  queryset = Farm.objects.all().select_related('farmer')
  serializer = FarmWithFarmerSerializer(queryset, many=True)
  context['farms'] = serializer.data
  return render(request, 'main/farmerswithcrops.html', context)

def farmerschedule(request: HttpRequest, farmer_id):
  print(farmer_id)
  context = {}
  queryset = Schedule.objects.all().select_related('farm').select_related('fertilizer').filter(farm__farmer__id=farmer_id).filter(farm__sowing_date__range = [timezone.now() - timedelta(days=1) - timedelta(days=1) * F('days_after_sowing'),timezone.now() - timedelta(days=1) * F('days_after_sowing')])
  serializer = ScheduleWithFarmAndFertilizer(queryset, many=True)
  context['schedules'] = serializer.data
  context['farmer'] = FarmerSerializer(Farmer.objects.get(id=farmer_id)).data
  return render(request, 'main/farmerschedule.html', context)


def totalCost(request: HttpRequest, farmer_id):
  context = {}
  queryset1 = Schedule.objects.all().select_related('farm').select_related('fertilizer').filter(farm__farmer__id=farmer_id)
  serializer1 = ScheduleWithFarmAndFertilizer(queryset1, many=True)
  context['schedules'] = serializer1.data
  queryset2 = queryset1.aggregate(total_cost=Sum(F('fertilizer__price_per_unit')*F('quantity')))
  context['total_cost'] = queryset2['total_cost']
  context['farmer'] = FarmerSerializer(Farmer.objects.get(id=farmer_id)).data
  return render(request, 'main/totalcost.html', context)
