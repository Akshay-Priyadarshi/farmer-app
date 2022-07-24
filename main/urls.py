from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()

router.register(r'farmers', views.FarmerViewSet)
router.register(r'farms', views.FarmViewSet)
router.register(r'crops', views.CropViewSet)
router.register(r'fertilizers', views.FertilizerViewSet)
router.register(r'schedules', views.ScheduleViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('farmerswithcrops/', views.farmerswithcrops, name='farmerswithcrops'),
    path('farmerschedule/<uuid:farmer_id>/', views.farmerschedule, name='farmerschedule'),
    path('totalcost/<uuid:farmer_id>/', views.totalCost, name='totalcost'),
    path('api/', include(router.urls)),
]