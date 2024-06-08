from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('schedule', views.ScheduleView)

urlpatterns = [
    path('', include(router.urls)),
]