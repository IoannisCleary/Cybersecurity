from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	context_dict = {}
	return render(request, 'trainingPortal/index.html', context_dict)
def about(request):
	context_dict = {}
	return render(request, 'trainingPortal/about.html', context_dict)