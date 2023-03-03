from django.shortcuts import render
from appone.models import app_one_person

def home(request):
    b=''
    if request.method == 'POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        Class=request.POST.get('Class')        
        data=app_one_person(name=name,age=age,gender=gender,Class=Class)
        data.save()
        b='your data has been sent sir you can go and check'
    print(b)
    return render(request,'appone/home.html',{'b':b})

def index(request):
    return render(request,'appone/index.html')

def homecopy(request):
    return render(request,'appone/homecopy.html')

def indexcopy(request):
    return render(request,'appone/indexcopy.html')
