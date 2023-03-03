from django.urls import path
from . import views



urlpatterns = [
    
    path('', views.home, name='home'),
    path('homecopy/', views.homecopy, name='homecopy'),

]
