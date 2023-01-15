from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('conference-publications/', views.pub, name='conference-publications'),
    path('single-conference-publications/<str:pk>', views.spub, name='single-conference-publications'),
    
]