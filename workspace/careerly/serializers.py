from rest_framework import serializers
from .models import JobPosting

class CareerlySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = ('id', 'jobtitle', 'company', 'location', 'jobType', 'datePosted', 'posting', 'logoimg')