from django.contrib import admin
from django.urls import path, include

from app.lecturers_manager.views import registerLecturer, lecturerProfile, postResults
from app.students_manager.views import assignMarks

urlpatterns = [
    path('register-lecturer', registerLecturer, name='register-lecturer'),
    path('lecturer-profile/<str:pk>', lecturerProfile, name='lecturer-profile'),
    path('marks/<str:pk>', assignMarks, name='choose-student'),
    path('post-results', postResults, name='choose-student'),
]
