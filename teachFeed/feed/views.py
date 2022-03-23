from django.shortcuts import render, HttpResponse

# Create your views here.
def feed(request):
    return render(request,"feed/feed.html")