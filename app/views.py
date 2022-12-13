from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .models import *


def chooseStudent(request):
    if request.method == "GET":
        students = Student.objects.all()
        return render(request, 'index.html', {"students": students})

    return redirect('/students')


def generateTranscript(request, pk):
    if request.method == "GET":
        page = request.GET.get('page', None)
        if page is not None:
            try:
                student = Student.objects.get(id=pk)
            except Student.DoesNotExist:
                return redirect('/students')

            if page == '2':
                results = QueryStudentResults(student, '2').getStudentsResults()

                return render(request, "modules_results.html", results)
            else:
                results = QueryStudentResults(student, '1').getStudentsResults()

                if results is None:
                    return HttpResponse("No Data")
                return render(request, "overall.html", results)
        else:
            return redirect(f'/transcript/{pk}?page=1')


class QueryStudentResults:
    def __init__(self, student, page):
        self.enrollment = None
        self.student = student
        self.page = page
        self.errors = ""
        self.status = True
        self.getEnrollment()

    def getEnrollment(self):
        try:
            self.enrollment = Enrollment.objects.get(student=self.student.id)
            print('okkkk')
        except Enrollment.DoesNotExist:
            print('dddd')
            self.status = False
            self.errors = "Enrollment not Found"
            return

    def constructOverallData(self, result):
        return {
            "surname": str(self.student.last_name).capitalize(),
            "dob": self.student.dob,
            "reg_no": self.student.reg_no,
            "gender": self.student.gender,
            "given_names": self.student.first_name,
            "adm_date": self.enrollment.starting_year,
            "grad_date": self.enrollment.end_year,
            "award_title": self.student.course,
            "class_award": result.class_award,
            "overall_gpa": result.credits
        }

    def studentSemesterResults(self):
        module_results = StudentModuleResult.objects.filter(student=self.student.id)
        nta_levels = CourseNTALevel.objects.filter(course=self.student.course.id)
        v = []
        for nta_level in nta_levels:
            nta_based_results = {
                "name": nta_level.nta_level.name,
                "semesters_results": []
            }
            for i in range(1, nta_level.nta_level.number_of_semesters + 1):
                z = dict()
                z['semester'] = f"SEMESTER {i}"
                modules = []
                modules_ = module_results.filter(semester=i, module__nta_level=nta_level.id)
                for module in modules_:
                    modules.append({
                        "code": module.module.code,
                        "name": module.module.name,
                        "grade": module.grade
                    })
                z['modules'] = modules
                z['semester_gpa'] = "3.123"
                nta_based_results['semesters_results'].append(z)

            v.append(nta_based_results)

        return {
            "results": v,
            "student": self.student
        }

    def studentOverallResults(self):
        results = OverallResult.objects.filter(student=self.student.id)
        if results.count() > 0 and self.enrollment is not None:
            result = results[0]
            return self.constructOverallData(result)

    def getStudentsResults(self):
        if self.page == '1':
            return self.studentOverallResults()
        else:
            return self.studentSemesterResults()
