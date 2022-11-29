from django.contrib import admin
from .models import *

_ = [Student, Class,
     Course, ClassModule, Category, Department,
     OverallResult, SemesterStudentResult, NTALevel,
     Module, Enrollment
     ]

for i in _:
    admin.site.register(i)
