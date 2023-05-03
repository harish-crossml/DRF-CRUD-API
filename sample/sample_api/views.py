from django.shortcuts import render
from rest_framework.views import APIView  
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response  
from rest_framework import status  
from .models import Students  
from .serializers import StudentSerializer  
# Create your views here.  

class StudentView(APIView):
    def get(self, request):
        students = Students.objects.all()    # Get all students
        serializer = StudentSerializer(students, many=True)   # create instance & set many=True for multiple objects.
        return Response(serializer.data)                      # return serialized data

    def post(self, request):
        serializer = StudentSerializer(data=request.data)   # create instance containing requested data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        student = Students.objects.get(id=id)    # get student with given id
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        student = Students.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# class StudentList(ListCreateAPIView):
#     queryset = Students.objects.all()
#     serializer_class = StudentSerializer

# class StudentDetail(RetrieveUpdateDestroyAPIView):
#     quesryset = Students.objects.all()
#     serializer_class = StudentSerializer