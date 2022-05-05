from urllib import response
from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
#from .serializers import TaskSerializer
#from .models import Task

# Create your views here.

@api_view(['GET'])
def ping_view(request):
    body = {
        f'"success"':True
    }
    return JsonResponse(body)

