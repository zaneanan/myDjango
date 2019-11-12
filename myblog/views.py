from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def homepage(request):
    
       
   
   return render(request, 'mainsite/homepage.html', locals())