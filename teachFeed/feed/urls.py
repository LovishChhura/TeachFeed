from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.feed, name="feed"),
    path('thanks/',views.thanks, name="thanks"),
]