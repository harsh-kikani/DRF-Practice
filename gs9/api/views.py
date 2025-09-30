# from django.shortcuts import render
# from .serializers import StudentSerializer
# from .models import Student
# from rest_framework import viewsets

# # Create your views here.

# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


from django.shortcuts import render
from .serializers import SingerSerializer, SongSerializer
from rest_framework import viewsets
from .models import Singer, Song

# Create your views here.

class SingerViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    
class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer