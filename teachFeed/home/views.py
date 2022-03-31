from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return render(request,'home/home.html')

def login(request):
    return HttpResponse('You are logged In')

def extra(request):
    return HttpResponse('This is extra')