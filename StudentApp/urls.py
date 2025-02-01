from django.urls import path
from . import views

app_name ="student_app"

urlpatterns = [
    path("",views.index,name="index"),
    path("students_list",views.students_list,name="students_list"),
    path("update/<int:id>",views.update_student,name="update_student"),
    path("delete/<int:id>",views.delete_student,name="delete_student"),
    path("insert_multiple_students",views.insert_multiple_students,name="insert_multiple_students"),
]