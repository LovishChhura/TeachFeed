from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.ifeed,name="ifeed"),
    path('tlogin/', views.tlogin,name="tlogin"),
    path('feedPanel/', views.feedPanel,name="feedPanel"),
    path('tlogout/', views.tlogout,name="tlogout")
]