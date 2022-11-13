from rest_framework import serializers
from .models import Careerly

class CareerlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Careerly
        fields = ('id', 'jobtitle', 'company')