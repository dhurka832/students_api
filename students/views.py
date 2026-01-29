from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm

def all_students(request):
    students = Student.objects.all()
    return render(request,'students/all_students.html',{'students':students})
    
def create_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all-students')
    else:
        form = StudentForm()
    return render(request,"students/student_create.html",{'form':form})
            
def update_student(request,pk):
    student = Student.objects.get(pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('all-students')
    else:
        form = StudentForm(instance=student)
    return render(request,"students/student_update.html",{'form':form})

def delete_student(request,pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return redirect('all-students')
