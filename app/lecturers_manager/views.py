from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from app.lecturers_manager.classes import PostResults
from app.lecturers_manager.serializers import LecturerSerializer
from app.models import Course, Lecturer, Class, Module


def registerLecturer(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            modules = Module.objects.all()
            classes = Class.objects.all()
            return render(request, 'registerLecturer.html', {"classes": classes, "modules": modules})
        elif request.method == "POST":
            serializer = LecturerSerializer(data=request.POST)
            if serializer.is_valid():
                print('Valid')
                lecturer = serializer.save()
                user = User()
                user.username = lecturer.email
                user.set_password(lecturer.cellphone)
                user.save()

                messages.info(request, "Successfully Registered")
                return redirect('/')

            print(serializer.errors)
            return redirect('/register-lecturer')

    return redirect('login-page')


def lecturerProfile(request, pk):
    if request.user.is_authenticated and request.user.is_staff:
        if request.method == 'GET':
            lecturer = Lecturer.objects.get(id=pk)
            return render(request, 'lecturer-profile.html', {"lecturer": lecturer})

    return redirect('login-page')


def postResults(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            lecturer = Lecturer.objects.get(user=request.user)
            PostResults(request, lecturer)
            return redirect('/')

    return redirect('login-page')


def listLecturers(request):
    lecturers = Lecturer.objects.all()
    return render(request, 'lecturers.html', {"lecturers": lecturers})

