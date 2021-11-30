from rest_framework.viewsets import ModelViewSet

from academy.models import Subject
from academy.serializers import SubjectSerializer

class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.select_related('academy').all()
    serializer_class = SubjectSerializer