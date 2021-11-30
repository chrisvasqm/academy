from rest_framework.viewsets import ModelViewSet

from academy.models import Student, Subject
from academy.serializers import StudentSerializer, SubjectSerializer

class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.select_related('academy').all()
    serializer_class = SubjectSerializer
    
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer