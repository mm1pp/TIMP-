import re
from django.http import HttpResponse
from django.shortcuts import render
from django import template

def home(request):
    return HttpResponse("Привет, Мир!")

def no_response(request):
    return HttpResponse()
    
def htmlll(request):
    return render(request, 'templates/index.html')

def html_static(request):
    return render(request, 'templates/static_handler.html')