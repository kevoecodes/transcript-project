"""transcript_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app.transcript.views import downloadTranscript
from app.views import *
from app.students_manager.views import registerStudent, studentProfile
from app.courses_manager.views import coursesList
from app.lecturers_manager.views import registerLecturer, listLecturers
from Authentications.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', studentsList, name='choose-student'),
    path('register-student', registerStudent, name='choose-student'),
    path('register-lecturer', registerLecturer, name='register-lecturer'),
    path('courses', coursesList, name='choose-student'),
    path('lecturers', listLecturers, name='choose-student'),
    path('login-page', Login_View, name='login-page'),
    path('transcript/<str:pk>', generateTranscript, name='student-transcript'),
    path('download-transcript/<str:pk>', downloadTranscript, name='download-transcript'),
    path('student-profile/<str:pk>', studentProfile, name='download-transcript')
]
