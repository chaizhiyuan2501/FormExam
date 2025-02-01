from django.shortcuts import render
from . import forms
from .models import Students
from django.forms import formset_factory,modelform_factory,modelformset_factory
from django.core.files.storage import FileSystemStorage
import os
# Create your views here.

def index(request):
    insert_form = forms.StudentsInfo(request.POST or None,request.FILES or None)
    if insert_form.is_valid():
        insert_form.save()
        insert_form = forms.StudentsInfo() # formの初期化
    return render(request, "index.html", context={
        "insert_form": insert_form
        })

def students_list(request):
    students = Students.objects.all()
    return render(request, "students_list.html", context={
        "students": students
        })

def update_student(request,id):
    students = Students.objects.get(id=id)
    update_form = forms.StudentUpdateForm(
        initial={
            "picture":students.name,
            "age":students.age,
            "grade":students.grade,
            "picture":students.picture,
        }
    )
    if request.method =="POST":
        update_form = forms.StudentUpdateForm(request.POST or None,request.FILES or None)
        if update_form.is_valid():
            students.name = update_form.cleaned_data["name"]
            students.age = update_form.cleaned_data["age"]
            students.grade = update_form.cleaned_data["grade"]
            picture = update_form.cleaned_data["picture"]
            # 画像が送られた場合
            if picture:
                fs =FileSystemStorage()
                file_name =fs.save(os.path.join("students",picture.name),picture)
                students.picture = file_name
            students.save()
    return render(
        request,"update_student.html",context={
            "update_form":update_form,
            "students":students
        }
    )

def delete_student(request,id):
    delete_form = forms.StudentDeleteForm(
        initial={
            "id":id
        }
    )
    if request.method =="POST":
        delete_form = forms.StudentDeleteForm(request.POST or None)
        if delete_form.is_valid():
            Students.objects.get(id=delete_form.cleaned_data["id"]).delete()
    return render(
        request,"delete_student.html",context={
            "delete_form":delete_form
        }
    )

def insert_multiple_students(request):
    StudentFormSet = modelformset_factory(Students,fields="__all__",extra=3)
    insert_form =StudentFormSet(request.POST or None,request.FILES or None)
    if insert_form.is_valid():
        insert_form.save()
    return render(request,"insert_multiple_students.html",context={
        "insert_form":insert_form
    })