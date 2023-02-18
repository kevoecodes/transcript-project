from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from app.lecturers_manager.serializers import LecturerSerializer
from app.models import Course, Lecturer


def registerLecturer(request):
    if request.user.is_authenticated and request.user.is_staff:
        if request.method == 'GET':
            courses = Course.objects.all()
            return render(request, 'registerLecturer.html', {"courses": courses})
        elif request.method == "POST":
            print(request.POST)
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
            #
            return redirect('/register-lecurer')

    return redirect('login-page')


def listLecturers(request):
    lecturers = Lecturer.objects.all()
    return render(request, 'lecturers.html', {"lecturers": lecturers})

