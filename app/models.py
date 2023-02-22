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

class NTALevel(models.Model):
    name = models.CharField(max_length=200, verbose_name='Level Name')
    number_of_semesters = models.IntegerField(null=False)

    def __str__(self):
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=200, verbose_name='Class Name')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    nta_level = models.ForeignKey(NTALevel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    MALE = "M"
    FEMALE = "F"

    GENDERS = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    first_name = models.CharField(max_length=200, verbose_name='Student First Names')
    last_name = models.CharField(max_length=200, verbose_name='Student Last Name')
    gender = models.CharField(max_length=200, choices=GENDERS, verbose_name='Student Gender')
    dob = models.DateField(null=False)
    reg_no = models.CharField(max_length=200, verbose_name='Registration Number')
    form_four = models.CharField(max_length=200, verbose_name='Form Four Index Number')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    ass_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.last_name.capitalize()} {self.first_name}"





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
        return f'{self.student} Enrollment'




class HOD(models.Model):
    name = models.CharField(max_length=200, verbose_name='HOD Name')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)



class Lecturer(models.Model):

    first_name = models.CharField(max_length=200, verbose_name='Lecturer First Names')
    last_name = models.CharField(max_length=200, verbose_name='Lecturer Last Name')
    cellphone = models.CharField(max_length=200, verbose_name='Lecturer Cellphone')
    email = models.EmailField(max_length=200, verbose_name='Email')
    ass_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.last_name.capitalize()} {self.first_name}"


class Module(models.Model):
    name = models.CharField(max_length=200, verbose_name='Module Name')
    code = models.CharField(max_length=200, verbose_name='Module Code')
    credits = models.IntegerField(null=False)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    nta_level = models.ForeignKey(NTALevel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class OverallResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    class_award = models.CharField(max_length=200, verbose_name="Classification Award")
    credits = models.FloatField(null=False)
    is_pass = models.BooleanField(null=False)

    def __str__(self):
        return f'{self.student} Overall'


class StudentModuleResult(models.Model):
    STATUSES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('F', 'F'),
    )
    SEMESTERS = (
        (1, 'Semester 1'),
        (2, 'Semester 2'),
        (3, 'Semester 3'),
        (4, 'Semester 4'),
        (5, 'Semester 5'),
        (6, 'Semester 6'),
    )
    semester = models.IntegerField(choices=SEMESTERS, null=False)
    student = models.ForeignKey(Student, verbose_name="Student", on_delete=models.SET_NULL, null=True)
    module = models.ForeignKey(Module, verbose_name="Module", on_delete=models.SET_NULL, null=True)
    ca = models.IntegerField(null=False)
    fe = models.IntegerField(null=False)
    grade = models.CharField(max_length=20, choices=STATUSES, verbose_name="Module Grade")

    def __str__(self):
        return f'{self.student} {self.module} Results'


class CourseNTALevel(models.Model):
    course = models.ForeignKey(Course, verbose_name="Course", on_delete=models.SET_NULL, null=True)
    nta_level = models.ForeignKey(NTALevel, verbose_name="NTA Level", on_delete=models.SET_NULL, null=True)
