from django.db import models
# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=200, verbose_name='Department Name')

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=200, verbose_name='Course Name')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=200, verbose_name='Student Name')
    reg_no = models.CharField(max_length=200, verbose_name='Registration Number')
    form_four = models.CharField(max_length=200, verbose_name='Form Four Index Number')
    admission = models.CharField(max_length=200, verbose_name='Admission Number')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    INCOMPLETE = 0
    COMPLETE = 1

    STATUSES = (
        (INCOMPLETE, 'Enrollment InComplete'),
        (COMPLETE, 'Enrollment Complete'),
    )

    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    starting_year = models.DateField(null=False)
    end_year = models.DateField(null=True, blank=True)
    enrollment_status = models.IntegerField(choices=STATUSES, null=False, verbose_name='Enrolment Status')

    def __str__(self):
        return f'{self.student.name} Enrollment'


class NTALevel(models.Model):
    name = models.CharField(max_length=200, verbose_name='Level Name')
    semester = models.CharField(max_length=200, verbose_name='Semester Name')

    def __str__(self):
        return self.name


class HOD(models.Model):
    name = models.CharField(max_length=200, verbose_name='HOD Name')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)


class Class(models.Model):
    name = models.CharField(max_length=200, verbose_name='Class Name')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    nta_level = models.ForeignKey(NTALevel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Module(models.Model):
    name = models.CharField(max_length=200, verbose_name='Module Name')
    code = models.CharField(max_length=200, verbose_name='Module Code')
    credits = models.IntegerField(null=False)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    nta_level = models.ForeignKey(NTALevel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class ClassModule(models.Model):
    Class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)
    module = models.ForeignKey(Module, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.Class.name} {self.module.name}'


class Category(models.Model):
    pass


class OverallResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    academic_year = models.CharField(max_length=200, verbose_name='Academic Year')
    credits = models.FloatField(null=False)
    is_pass = models.BooleanField(null=False)


class SemesterStudentResult(models.Model):
    PASSED = 0
    NOT_PASSED = 0
    STATUSES = (
        (PASSED, 'Passed'),
        (NOT_PASSED, 'Not Passed'),
    )
    SEMESTERS = (
        (1, 'Semester 1'),
        (2, 'Semester 2'),
    )
    semester = models.IntegerField(choices=SEMESTERS, null=False)
    module = models.ForeignKey(Module, on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    ca = models.FloatField(verbose_name='Continuous Assessments', null=False)
    fe = models.FloatField(verbose_name='Final Examination', null=False)
    status = models.IntegerField(choices=STATUSES, null=False)

    def __str__(self):
        return f'{self.student.name} Results'
