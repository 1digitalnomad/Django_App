from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = 'hello, I am the index for the second app.'
    return HttpResponse(response)
