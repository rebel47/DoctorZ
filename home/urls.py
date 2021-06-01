from home.forms import editProfile
from django.contrib import admin
from django.urls import path
from home import views
from .views import UpdateView
from django.conf.urls import *
from .views import editProfile

urlpatterns = [
    path('',views.index, name="home"),
    path('home',views.index, name="home"),
    path('dashboard',views.dashboard, name="dashboard"),
    path('profile',views.profile, name="profile"),
    # path('profile/edit',views.editProfile, name="editProfile"),
    # path('profile/edit',editProfile.as_view(), name="editProfile"),
    path('service',views.service, name="service"),
    # path('login',views.loginUser, name="login"),
    # path('logout',views.logoutUser, name="logout"),
    # path('signup',views.signupUser, name="signup"),
]