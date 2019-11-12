from django.contrib import admin
from django.urls import path
from myblog.views import homepage

urlpatterns = [
    path('',homepage),
]