from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
import json
from .serializers import BookSerializer
# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer

@csrf_protect
def add_book(request):
    if request.user.is_authenticated: 
        print(request.POST)
        print(request.FILES)
        book = Book.objects.create(author=request.POST['author'],title=request.POST['title'],description=request.POST['description'],poster_image=request.FILES['poster_image'])
        return HttpResponse("Book successfully added.")
    else:
        return HttpResponse("Permission Denied") 
     
@csrf_protect
def add_favourites(request):
   if request.user.is_authenticated:
        register_dict = json.loads(list(request.POST.dict().keys())[0])
        book_title = register_dict['title']
        queryset = Book.objects.all().get(title=book_title)
        user = User.objects.get(pk= request.user.id)
        user.profile.books.add(queryset)
        return HttpResponse("Book successfully added to favourites.")
   else:
        return HttpResponse("Permission Denied")


@csrf_protect
def remove_favourite_book(request):
    if request.user.is_authenticated:
        register_dict = json.loads(list(request.POST.dict().keys())[0])
        book_title = register_dict['title']
        queryset = Book.objects.all().get(title=book_title)
        user = User.objects.get(pk= request.user.id)
        user.profile.books.remove(queryset)
        return HttpResponse("Book successfully removed from favourites.")
    else:
        return HttpResponse("Permission Denied")

@csrf_protect
def list_favourites(request):
    if request.user.is_authenticated:
        user = User.objects.get(pk= request.user.id)
        return HttpResponse(json.dumps(BookSerializer(user.profile.books.all(),many=True).data))
    else:
        return HttpResponse("Permission Denied")

def isLoggedin(request):
    print(request.user.id)
    if request.user.is_authenticated:
        print("Logged in")
        return HttpResponse("true")
    else:
        print("Not autheticated")
        return HttpResponse("false")

@csrf_protect
def signup(request):
    if request.method == 'POST':
        register_dict = json.loads(list(request.POST.dict().keys())[0])
        form = UserCreationForm(register_dict)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponse("authentication successful")
        else:
            return HttpResponse("User already exists.")
    else:
        return HttpResponse("Error: not a POST request.")

@csrf_protect
def signin(request):
    if request.method == 'POST':
        register_dict = json.loads(list(request.POST.dict().keys())[0])
        username = register_dict['username']
        password = register_dict['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("Login successful")
        else:
            return HttpResponse("Invalid credentials.")
    else:
        return HttpResponse("Error: not a POST request.")

@csrf_protect
def signout(request):
    try:
        logout(request)
        return HttpResponse("Logged out")
    except:
        return  HttpResponse("Error")
