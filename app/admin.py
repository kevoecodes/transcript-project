from django.contrib import admin
from .models import *

_ = [Student, Class,
     Course, Department,
     OverallResult, StudentModuleResult, NTALevel,
     Module, Enrollment, CourseNTALevel
     ]

for i in _:
    admin.site.register(i)
