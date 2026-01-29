from django.urls import path
from . import views

urlpatterns = [
    path('students/',views.studentView),
    path('students/<int:pk>/',views.student_DetailView),
    path('students/create/',views.student_create),
    path('students/update/<int:pk>/',views.student_update),
    path('students/delete/<int:pk>/',views.student_delete)
]
