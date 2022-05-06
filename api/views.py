from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import json
from .helpers import queryTags
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
    #Parse request
    try: 
        body = json.loads(request.body.decode("utf-8"))
    except:
        return JsonResponse({"error": "invalid json format in request"},status=status.HTTP_400_BAD_REQUEST)
    #Handle tag errors
    if 'tags' not in body:
        #Tag error
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
    tags = body['tags']
    posts = queryTags(tags)
    posts.sort(key=lambda x: x.get(sortBy),reverse=True if direction=='desc' else False)
    return JsonResponse({"posts":posts},status=status.HTTP_200_OK)

