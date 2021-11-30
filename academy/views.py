from django.db.models.query import QuerySet
from rest_framework.viewsets import ModelViewSet

from academy.models import Enrollment, Student, Subject
from academy.serializers import AddSubjectSerializer, EnrollmentSerializer, StudentSerializer, SubjectSerializer

class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.select_related('academy').all()
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddSubjectSerializer
        
        return SubjectSerializer
    
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class EnrollmentViewSet(ModelViewSet):
    queryset = Enrollment.objects.select_related('student').select_related('subject').all()
    serializer_class = EnrollmentSerializer