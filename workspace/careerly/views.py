from django.shortcuts import render
import sys
import os
import json
import re
from django.http import HttpResponse
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

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