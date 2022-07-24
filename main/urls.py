from django.urls import path, include
from rest_framework import routers
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from . import views

router = routers.SimpleRouter()

router.register(r'farmers', views.FarmerViewSet)
router.register(r'farms', views.FarmViewSet)
router.register(r'crops', views.CropViewSet)
router.register(r'fertilizers', views.FertilizerViewSet)
router.register(r'schedules', views.ScheduleViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('api-schema/',get_schema_view(title='Farmerz API Schema'),name='api-schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'api-schema'}
    ), name='swagger-ui'),
    path('farmerswithcrops/', views.farmerswithcrops, name='farmerswithcrops'),
    path('farmerschedule/<uuid:farmer_id>/', views.farmerschedule, name='farmerschedule'),
    path('totalcost/<uuid:farmer_id>/', views.totalCost, name='totalcost'),
    path('api/', include(router.urls)),
]