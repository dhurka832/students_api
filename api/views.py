from students.models import Student 
from .serializers import StudentSerializer
from rest_framework import status 
from rest_framework.response import Response 
from rest_framework.decorators import api_view

@api_view(['GET'])
def studentView(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def student_DetailView(request,pk):
    if request.method == "GET":
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def student_create(request):
    if request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['PUT'])
def student_update(request,pk):
    student = Student.objects.get(pk=pk)
    serializer = StudentSerializer(student,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def student_delete(request,pk):
    student = Student.objects.get(pk=pk)
    if request.method == "DELETE":
        student.delete()
        return Response({'message':'Post Deleted'})
    return Response(status=status.HTTP_404_NOT_FOUND)