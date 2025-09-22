from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

class StudentAPI(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)   
    
    def delete(self, request, pk, format=None):
        stu = get_object_or_404(Student, id=pk)
        stu.delete()
        return Response({'msg': 'Data Deleted'}, status=status.HTTP_200_OK)



#---------Function Base API--------------- 

# @api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
# def student_api(request, pk=None):
#     if request.method == 'GET':
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)
        
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data created'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.H)
    
#     if request.method == 'PUT':
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Complete Data Updated'})
#         return Response(serializer.errors)
    
    
#     if request.method == 'PATCH':
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Partial Data Updated'})
#         return Response(serializer.errors)
    
    
#     if request.method == 'DELETE':
#         id = pk
#         stu = Student.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg':'Data Deleted'})


#------For Third Party application----

# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def student_api(request):
#     if request.method == 'GET':
#         id = request.data.get('id')
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)
        
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data created'})
#         return Response(serializer.errors)
    
#     if request.method == 'PUT':
#         id = request.data.get('id')
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Updated'})
#         return Response(serializer.errors)
    
#     if request.method == 'DELETE':
#         id = request.data.get('id')
#         stu = Student.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg':'Data Deleted'})























#--GET----
# @api_view()
# def hello_world(request):
#     return Response({'msg':'Hello World'})

#--POST----
# @api_view(['POST'])
# def hello_world(request):  
#     if request.method == "POST":
#         print(request.data)
#         return Response({'msg':'This is POST Request'})
    
    
# @api_view(['GET','POST'])
# def hello_world(request):
#     if request.method == "GET":
#         return Response({'msg':'This is GET Request'})
    
#     if request.method == "POST":
#         print(request.data)
#         return Response({'msg':'This is POST Request'})