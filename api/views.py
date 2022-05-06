from urllib import response
from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
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
    #Handle tag errors
    if 'tags' not in body:
        return JsonResponse({"error": "tags parameter is required"},status=status.HTTP_400_BAD_REQUEST)
    #Default values
    sortBy = 'id'
    direction = 'asc'
    #Handle invalid sortBy
    if 'sortBy' in body:
        if body['sortBy'] not in ['id','reads','likes','popularity']:
            #Invalid value
            return JsonResponse({"error": "sortBy parameter is required"},status=status.HTTP_400_BAD_REQUEST)
        sortBy = body['sortBy']
    #Handle invalid direction 
    if 'direction' in body:
        if body['direction'] not in ['desc','asc']:
            #Invalid value
            return JsonResponse({"error": "direction parameter is required"},status=status.HTTP_400_BAD_REQUEST)
        direction = body['direction']

    return Response(f'test {sortBy} {direction}')

