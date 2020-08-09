from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializers
from .models import Task
# Create your views here.


@api_view(['GET'])
def api(request):
    api_urls = {
        'List': '/task-list/',
        'Detail Views': '/task-detail/<str:pk>',
        'Update': '/task-update/<str:pk>',
        'Delete': '/task-delete/<str:pk>'
    }

    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    task = Task.objects.all()
    serializer = TaskSerializers(task,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializers(task,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response('Created Succesfully')

@api_view(['POST'])
def taskUpdate(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializers(instance=task,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response('Updated Succesfully')

@api_view(['DELETE'])
def taskDelete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response('Delete Succesfully')