from django.urls import path
from home import views
from django.conf.urls import *

urlpatterns = [
    path('',views.index, name="home"),
    path('home',views.index, name="home"),
     path('book-appointment',views.dashboard, name="book-appointment"),
    path('profile',views.profile, name="profile"),
    path('booked-sessions',views.service, name="booked-sessions"),
    path('covid-19',views.covid, name="covid-19"),
   
]