from django.shortcuts import render
from django.http import HttpResponse

# Here we define a basic view response, just return text Hello World
def home(request):
    return HttpResponse('Hello, World!')
