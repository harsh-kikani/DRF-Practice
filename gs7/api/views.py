# from django.shortcuts import render
# from .serializers import StudentSerializer
# from rest_framework.generics import ListAPIView
# from .models import Student
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import SearchFilter
# from rest_framework.filters import OrderingFilter

# Create your views here.

# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     filter_backends = [DjangoFilterBackend]
#     # filterset_fields = ['city']
#     filterset_fields = ['name','city']


# class StudentList(ListAPIView):
#     # queryset = Student.objects.filter(passby='user1')
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def get_queryset(self):
#         user = self.request.user
#         return Student.objects.filter(passby=user)
    
    
# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     filter_backends = [SearchFilter]
#     search_fields = ['city']
    # search_fields = ['name','city']
    # search_fields = ['^name']
    
# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     filter_backends = [OrderingFilter]
#     ordering_fields = ['name','city']

# from django.shortcuts import render
# from .serializers import StudentSerializer
# from rest_framework.generics import ListAPIView
# from .models import Student
# from .mypaginations import MyPageNumberPagination

# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     pagination_class = MyPageNumberPagination


from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student
from .mypaginations import MyCursorPagination


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # pagination_class = MyLimitOffsetPagination
    pagination_class = MyCursorPagination