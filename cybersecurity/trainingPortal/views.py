from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Hey everyone <br/> <a href='/trainingPortal/about'>About</a>")
def about(request):
	return HttpResponse("About page <a href='/trainingPortal'>Back</a>")