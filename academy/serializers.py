from re import sub
from rest_framework import serializers

from .models import Subject

class SubjectSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField(method_name='get_total_price')
    
    class Meta:
        model = Subject
        fields = ['id', 'credits', 'price_per_credit', 'academy', 'total_price']
        
    def get_total_price(self, subject: Subject):
        return subject.credits * subject.price_per_credit