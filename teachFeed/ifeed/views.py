from django.shortcuts import render, HttpResponse, redirect
from .models import Taccess
from django.contrib import messages
from feed.models import Department, Teacher, Subject, Feed
# Create your views here.
def ifeed(request):
    return render(request,'ifeed/ifeedHome.html')

def tlogin(request):
    if request.method == "POST":
        acscode = request.POST['acscode']
        access= Taccess.objects.all()
        for i in access:
            if acscode==i.accesscd:
                stDepartment={'stDepartment':acscode}
                return redirect('feedPanel')
            if acscode!=i.accesscd:
                messages.error(request, "Invalid Credentials")


    return redirect('ifeed')

def feedPanel(request):
    dep = Department.objects.all()
    teach = Teacher.objects.all()
    sub = Subject.objects.all()
    params = {'dep': dep, 'teach': teach, 'sub': sub}
    #print(params)
    if request.method=="POST":
        return render(request,'ifeed/ifeed.html',params)
    return render(request,'ifeed/feedPanel.html',params)

def tlogout(request):
    return redirect('ifeed')