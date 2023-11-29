# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from .serializer import UserSerializer, PostSerializer, CommentSerializer, LikeSerializer, EventSerializer, InterestSerializer
from .models import User, Post, Comment, Like, Event, Interest
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login, logout, authenticate

# CONTROLLER/ To CONVER A JX
class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

def register(request):
    try:
        user = User.objects.create_user(username=request.POST['username'],
                                        password=request.POST['password1'],
                                        email=request.POST['email'])
        user.save()
        login(request, user)
        token, _ = Token.objects.get_or_create(user=user)
        return Response("User created successfully", token.key)
    except IntegrityError:
        return Response("Username already exists")
    
"""
def login(request):
    username = request.POST.get('username')#username = request.POST.get('username')
    password = request.POST.get('password')#password = request.POST.get('password')
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response("Usuario inválido")
    pwd_valid = check_password(password, user.password)
    if not pwd_valid:
        return Response("Contraseña inválida")
    token, _ = Token.objects.get(user=user)
    #token, _ = Token.objects.get_or_create(user=user)
    return Response(token.key, user)# return Response(token.key)
"""
"""
@csrf_exempt
def event_list(request):
    
    if request.method == 'GET':
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        user_id = request.user.id
        data = JSONParser().parse(request)
        serializer = EventSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



def demo_add(request):
user_id=request.user.id
tutorial_data = JSONParser().parse(request)
demo_serializer = DemoSerializer(data=tutorial_data)

if demo_serializer.is_valid():
    demo_serializer.save({"user_id":user_id ,"description":tutorial_data['description']})
    return JsonResponse({"result": True})
return JsonResponse({"result":False,"msg":"Invalid validation"}, status=status.HTTP_400_BAD_REQUEST)



@csrf_exempt
def event_detail(request, pk):
    
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EventSerializer(event)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EventSerializer(event, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        event.delete()
        return HttpResponse(status=204)
"""

def signin(request):
    if request.method == 'GET':
        return render(request)
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        #print(request.POST)
        if user is None:
            return render(request,{'error':'Username or password is incorrect'})
        else:
            login(request, user)
            token, _ = Token.objects.get(user=user)
            return Response(token.key, user)

def verify(request):
    try:
        user = User.objects.get(user=user)
    except User.DoesNotExist:
        serializer = UserSerializer(user)
        return Response(serializer.data)

def getUsers(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, safe=False)
    
def getUser(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=404)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)


class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CommentView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class LikeView(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()


class EventView(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

class InterestView(viewsets.ModelViewSet):
    serializer_class = InterestSerializer
    queryset = Interest.objects.all()
