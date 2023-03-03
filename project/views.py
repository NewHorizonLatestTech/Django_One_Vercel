from django.http import HttpResponse
from django.shortcuts import render
from . import views


def home(request):
    # print(request.GET)
    print(request.POST)
    return render(request,'home.html')


def contact(request):
    return render(request,'contact.html')
                  
                  
def index(request):
    return render(request,'index.html')
                  
def about(request):  
    return render(request,'about.html')
                  
def homecopy(request):
    return render(request,'homecopy.html')
                         
def contactcopy(request):
    return render(request,'contactcopy.html')
                  
def aboutcopy(request):  
    return render(request,'aboutcopy.html')
                     
def indexcopy(request):  
    return render(request,'indexcopy.html')
                     