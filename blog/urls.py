
from django.urls import path
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', views.glav, name='glav'),

    path('url/', views.urlform, name='url'),
    path('about', views.contacti, name='contacti')
    
  
    
   
    
]
