from django.shortcuts import render, HttpResponse, redirect
from .models import Taccess
from django.contrib import messages
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
    if request.method=="POST":
        return render(request,'ifeed/ifeed.html')
    return render(request,'ifeed/feedPanel.html')

def tlogout(request):
    return redirect('ifeed')