from django.shortcuts import render,HttpResponse
from django.conf.urls import handler404, handler500

# Create your views here.
def index(request):
	return render(request,'index.html')
	
def about(request):
	return render(request,'about.html')
	
def services(request):
	return render(request,'sorry.html')
	
def projects(request):
	return render(request,'projects.html')
	
def contact(request):
	return render(request,'sorry.html')
	
def error_404(request, exception):
    return render(request, 'sorry.html', status=404)
