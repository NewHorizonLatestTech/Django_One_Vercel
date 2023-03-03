from django.shortcuts import render

def home(request):
    return render(request,'apptwo/home.html')
                  
def homecopy(request):
    return render(request,'apptwo/homecopy.html')
