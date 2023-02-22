from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from num2words import num2words
from app.models import Course, Enrollment, Student, StudentModuleResult, CourseNTALevel, Class
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


def get_classes(i, o=0):
    if i == "0_1":
        if o == 0:
            return "nav-link active"
        else:
            return "tab-pane fade show active"
    else:
        if o == 0:
            return "nav-link"
        return "tab-pane fade"


def studentProfile(request, pk):
    if request.user.is_authenticated and request.user.is_staff or request.user.last_name == '3':
        if request.method == "GET":
            data = dict(request.POST.dict())
            print(data)
            try:
                student = Student.objects.get(id=pk)
                course_nta_levels = CourseNTALevel.objects.filter(course=student.course)
                results = StudentModuleResult.objects.filter(student=student)
                semester_resutls = []
                for j in range(0, len(course_nta_levels)):
                    for i in range(1, course_nta_levels[j].nta_level.number_of_semesters + 1):
                        semester_resutls.append({
                            "id": f"{num2words(j, to = 'ordinal')}_semester_{num2words(36, to = 'ordinal')}-tab",
                            "href": f"{num2words(j, to = 'ordinal')}_semester_{i}",
                            "name": f"{course_nta_levels[j].nta_level.name} Semester {i}",
                            "classes": get_classes(f"{j}_{i}"),
                            "main_classes": get_classes(f"{j}_{i}", 1),
                            "results": results.filter(semester=i)
                        })
                print(semester_resutls)
            except Exception as e:
                print(e)
                return redirect('/students')
            results = StudentModuleResult.objects.filter(student=student)
            return render(request, 'profile.html', {
                "student": student, "id": pk, "semester_results": semester_resutls, "results": results})

    return redirect('login-page')


def assignMarks(request, pk):
    if request.method == "GET":
        try:
            ass_class = Class.objects.get(id=pk)
            students = Student.objects.filter(ass_class=ass_class)
            return render(request, 'assign-marks.html', {
                "students": students, "id": pk, "class": ass_class})

        except Exception as e:
            print(e)
            return redirect('/login-page')

    if request.method == "POST":
        print(request.POST)
        return redirect(f'/assign-marks/{pk}')
