from django.db.models.query import QuerySet
from rest_framework.viewsets import ModelViewSet

from academy.models import Enrollment, Student, Subject
from academy.serializers import EnrollmentSerializer, StudentSerializer, SubjectSerializer

class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.select_related('academy').all()
    serializer_class = SubjectSerializer
    
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class EnrollmentViewSet(ModelViewSet):
    queryset = Enrollment.objects.select_related('student').select_related('subject').all()
    serializer_class = EnrollmentSerializer