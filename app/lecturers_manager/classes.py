from app.lecturers_manager.serializers import StudentModuleResultSerializer, ResultsAssignmentSerializer
from app.models import StudentModuleResult


class PostResults:
    def __init__(self, request, lecturer):
        self.lecturer = lecturer
        self.semester = lecturer.ass_class.current_level
        self.module = lecturer.module
        data = dict(request.POST.lists())
        del data['csrfmiddlewaretoken']
        self.registerAssignMarks()
        for key in data:
            print(key[5:])
            print("CA", int(data[key][0]))
            print("FE", int(data[key][1]))
            self.putMarks(key[5:], int(data[key][0]), int(data[key][1]))

    def putMarks(self, student_id, ca, fe):
        data = {
            "module": self.module.id,
            "fe": fe,
            "ca": ca,
            "grade": self.deduceGrade(ca, fe),
            "student": student_id,
            "semester": self.semester
        }
        try:
            results = StudentModuleResult.objects.get(
                module=self.module,
                student_id=student_id,
                semester=self.semester
            )
            serializer = StudentModuleResultSerializer(instance=results, data=data)
            if serializer.is_valid():
                serializer.save()
            print(serializer.errors)
        except StudentModuleResult.DoesNotExist:
            serializer = StudentModuleResultSerializer(data=data)
            if serializer.is_valid():
                serializer.save()

            print("Assifn", serializer.errors)

    def registerAssignMarks(self):
        data = {
            "lecturer": self.lecturer.id,
            "module": self.module.id,
            "semester": self.semester,
            "nta_level": self.lecturer.ass_class.nta_level.id
        }
        serializer = ResultsAssignmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

    @staticmethod
    def deduceGrade(ca, fe):
        total = int(ca) + int(fe)
        if total > 90:
            return "A"
        elif total > 70:
            return "B"

        elif total > 50:
            return "C"

        elif total > 30:
            return "D"

        else:
            return "F"



