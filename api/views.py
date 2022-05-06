from urllib import response
from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
#from .serializers import TaskSerializer
#from .models import Task

# Create your views here.

@api_view(['GET'])
def ping_view(request):
    body = {
        f'"success"':True
    }
    return JsonResponse(body)

@api_view(['GET'])
def post_view(request):
    body = json.loads(request.body.decode("utf-8"))
    if not body['tags']:
        return Response('placeholder error')
    return Response('test')

