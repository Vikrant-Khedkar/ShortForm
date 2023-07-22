from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .views import VideoApi,VideoViewSet,all_videos,upload
router = routers.DefaultRouter()
router.register('video',VideoApi)
router.register('videos',VideoViewSet)


urlpatterns = [
    path("api/",include(router.urls)),
    path('videos/', all_videos, name='all_videos'),
    path('upload/',upload,name='upload'),

]