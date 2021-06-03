from django.shortcuts import render,HttpResponse

# Create your views here.
 
def world(request):
    return HttpResponse("<h1>Hello World.</h1><h2>Welcome to AkashTechnolabs Family</h2>")