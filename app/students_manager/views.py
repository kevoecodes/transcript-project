from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from app.models import Course, Enrollment, Student, StudentModuleResult
from app.students_manager.serializer import StudentSerializer


def registerStudent(request):
    if request.user.is_authenticated and request.user.is_staff:
        if request.method == 'GET':
            courses = Course.objects.all()
            return render(request, 'registerStudent.html', {"courses": courses})
        elif request.method == "POST":
            print(request.POST)
            serializer = StudentSerializer(data=request.POST)
            if serializer.is_valid():
                print('Valid')
                student = serializer.save()
                user = User()
                user.username = student.reg_no
                user.set_password(student.reg_no)
                user.save()

                enroll = Enrollment()
                enroll.student = student
                enroll.starting_year = request.POST['starting_year']
                enroll.end_year = request.POST['end_year']
                enroll.enrollment_status = Enrollment.COMPLETE
                enroll.save()

                messages.info(request, "Successfully Registered")
                return redirect('/')

            print(serializer.errors)
            #
            # messages.error(request, serializer.errors)
            return redirect('/register-student')

    return redirect('login-page')


def studentProfile(request, pk):
    if request.user.is_authenticated and request.user.is_staff or request.user.last_name == '3':
        if request.method == "GET":
            data = dict(request.POST.dict())
            print(data)
            try:
                student = Student.objects.get(id=pk)
            except Exception as e:
                print(e)
                return redirect('/students')
            results = StudentModuleResult.objects.filter(student=student)
            return render(request, 'profile.html', {"student": student, "id": pk, "results": results})

    return redirect('login-page')