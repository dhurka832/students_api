from django.urls import path 
from . import views  

urlpatterns = [
    path('students/',views.all_students,name="all-students"),
    path('create/',views.create_student,name="create-student"),
    path('update/<int:pk>/',views.update_student,name="update-student"),
    path('delete/<int:pk>/',views.delete_student,name="delete-student"),
]
