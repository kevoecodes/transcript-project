from django.shortcuts import render

from app.models import Course, CourseNTALevel
from django.shortcuts import render, redirect


def coursesList(request):
    data = []
    courses = Course.objects.all()
    for course in courses:
        nta_levels = CourseNTALevel.objects.filter(course=course)

        data.append({
            "id": course.id,
            "name": course.name,
            "nta_levels": nta_levels
        })
        print(data)
    return render(request, 'courses.html', {"courses": data})
