from django.urls import path
from . import views


urlpatterns = [  
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('homecopy/', views.homecopy, name='homecopy'),
    path('indexcopy/', views.indexcopy, name='indexcopy'),
]
