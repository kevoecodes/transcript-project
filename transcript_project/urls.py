from django.contrib import admin
from django.urls import path, include

from app.transcript.views import downloadTranscript
from app.views import *
from app.students_manager.views import registerStudent, studentProfile, assignMarks
from app.courses_manager.views import coursesList
from app.lecturers_manager.views import registerLecturer, listLecturers
from Authentications.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', studentsList, name='choose-student'),
    path('assign-marks/<str:pk>', assignMarks, name='choose-student'),
    path('register-student', registerStudent, name='choose-student'),
    path('courses', coursesList, name='choose-student'),
    path('lecturers', listLecturers, name='choose-student'),
    path('register-lecturer', registerLecturer, name='register-lecturer'),
    path('login-page', Login_View, name='login-page'),
    path('logout-user', Logout, name='logout-user'),
    path('transcript/<str:pk>', generateTranscript, name='student-transcript'),
    path('download-transcript/<str:pk>', downloadTranscript, name='download-transcript'),
    path('student-profile/<str:pk>', studentProfile, name='download-transcript'),

    path('', include('app.lecturers_manager.urls'))
]
