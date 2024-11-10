from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework.response import Response
from .models import User
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime


from rest_framework import status
from .models import Todo                 #task1
from .serializers import TodoSerializer


class Register(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class Login(APIView):
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]

        user = User.objects.filter(email = email).first()

        if user is None:
            raise AuthenticationFailed("user not found")
        
        if not user.check_password(password):
            raise AuthenticationFailed("incorrect password")
        

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            "jwt": token
        }

        return response
    
    
class Logout(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message' : "logged_out"
        }
        return response
    

class userView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed("Not Authenticated")
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Not Authenticated")

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)


# from task 1

@api_view(['POST'])
def add_task(request):

    token = request.COOKIES.get('jwt')
    if not token:
        raise AuthenticationFailed("Not Authenticated")
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed("Not Authenticated")
    
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


@api_view(['DELETE'])
def delete_task(request, id):

    token = request.COOKIES.get('jwt')
    if not token:
        raise AuthenticationFailed("Not Authenticated")
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed("Not Authenticated")
    
    todo = Todo.objects.get(id=id)
    todo.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def update_task(request, id):
    token = request.COOKIES.get('jwt')
    if not token:
        raise AuthenticationFailed("Not Authenticated")
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed("Not Authenticated")
    

    todo = Todo.objects.get(id=id)
    
    if request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def show(request):
    token = request.COOKIES.get('jwt')
    if not token:
        raise AuthenticationFailed("Not Authenticated")
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed("Not Authenticated")
    
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)  

