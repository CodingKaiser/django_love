# Create your views here.
from django.shortcuts import render

from django.http import HttpResponse

from .models import CodeSnippet

def index(request):

    return HttpResponse("<h1>Hello World</h1>")
