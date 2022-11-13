from django.shortcuts import render
import sys
import os
import json
import re
from django.http import HttpResponse
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

from rest_framework.decorators import api_view

from rest_framework import status

from rest_framework import viewsets
from .serializers import CareerlySerializer
from rest_framework.response import Response
from .models import JobPosting

# def index(request):
#     return HttpResponse("Hello, world. You're at the careerly index.")


# Landing Page
def index(request):
    if request.method == 'GET':
        return render(request, 'careerly/index.html',
                      {
                      }
            )

# Main Page
def getMainPage(request):
    if request.method == 'GET':
        return render(request, 'careerly/main.html',
                      {
                      }
            )

@api_view(['GET', 'POST'])
def job_list(request):
    # Initial load of the page
    if request.method == 'GET':
        data = JobPosting.objects.all()

        serializer = CareerlySerializer(data, context={'request': request}, many=True)
        print("Get request")
        return Response(serializer.data)

    # When filter is used by the user
    elif request.method == 'POST':
        serializer = CareerlySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)