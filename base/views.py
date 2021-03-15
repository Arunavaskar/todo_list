from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def taskList(request):
    return HttpResponse('to do list')