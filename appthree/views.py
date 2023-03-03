from django.shortcuts import render

def home(request):
    return render(request,'appthree/home.html')

def homecopy(request):
    return render(request,'appthree/homecopy.html')
