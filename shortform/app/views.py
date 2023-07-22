from django.shortcuts import render
from .models import Video
from rest_framework import viewsets
from .serializers import VideoSerializer
from django.http import HttpResponse

class VideoApi(viewsets.ModelViewSet):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
   
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Video = serializer.save()
        return HttpResponse("uploaded")

class VideoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

def all_videos(request):
    return render(request, 'index.html')


def upload(request):
    return render(request, 'upload.html')