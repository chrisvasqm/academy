from rest_framework import serializers

from .models import Subject

class SubjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Subject
        fields = ['id', 'credits', 'price_per_credit', 'academy']