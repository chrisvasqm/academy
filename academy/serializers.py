from rest_framework import serializers
from .models import Academy, Subject

class AcademySerializer(serializers.ModelSerializer):
    class Meta:
        model = Academy
        fields = ['id', 'name', 'created_at']

class SubjectSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField(method_name='get_total_price')
    academy = AcademySerializer(read_only=True)
    
    class Meta:
        model = Subject
        fields = ['id', 'name', 'credits', 'price_per_credit', 'academy', 'total_price']
        
    def get_total_price(self, subject: Subject):
        return subject.credits * subject.price_per_credit