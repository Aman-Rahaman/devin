from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer

@api_view(['POST'])
def add_task(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['DELETE'])
def delete_task(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update_task(request, id):
    todo = Todo.objects.get(id=id)
    
    if request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def show(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)  

