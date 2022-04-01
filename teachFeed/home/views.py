from django.shortcuts import render, HttpResponse, redirect
from .models import Access
from django.contrib import messages
# Create your views here.

def home(request):

    return render(request,'home/home.html')

def login(request):
    if request.method == "POST":
        acscode = request.POST['acscode']
        access= Access.objects.all()
        for i in access:
            if acscode==i.accesscd:
                stDepartment={'stDepartment':acscode}
                return redirect('feed')
            if acscode!=i.accesscd:
                messages.error(request, "Invalid Credentials")


    return redirect('home')

def extra(request):
    return HttpResponse('This is extra')