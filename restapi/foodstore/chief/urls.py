from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import chiefViewSet

router=DefaultRouter()
router.register('',chiefViewSet,basename='chief')
app_name='chief'

urlpatterns = [
    path('',include(router.urls))
]
