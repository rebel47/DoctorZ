from django.db import models
from django.db.models import fields
from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages

from django.core.mail import send_mail
from .models import Servicetype, Service
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from .forms import editProfile


# Create your views here.
def index(request):
    return render(request, 'landingPage.html')

def dashboard(request):
    if request.method == 'GET':
        services = list(Servicetype.objects.values())
        return render(request, 'dashboard.html', {'services':services})

def profile(request):
    return render(request, 'profile.html')



# def editProfile(request):
#     return render(request, 'editProfile.html')

# class editProfile(UpdateView):
#     models = Users
#     template_name = 'editProfile.html'
#     fields = ('username','email','firstname','lastname')

    # what I have change to for upper code
    # admin.py mein Users register remover that
    # urls.py mein update import remove that and profile/edit mein bhi
    # views mein bhi update import kra hai

# def editProfile(request):
#     if request.method == 'POST':
#         form = User(request.POST, request.user)

#         if form.is_valid():
#             form.save()
#             return redirect(('profile'))
#     else:
#         form = User(request.user)
#         args = {'form': form}
#         return render(request, 'editProfile.html')

# class editProfile(generic.UpdateView):
#     model = User
#     template_name = "editProfile.html"
#     fields = ['username','email','password','firstname','lastname']
#     success_url = reverse_lazy('profile')
    
    



def service(request):
    
    if request.method == 'GET':

        services = list(Service.objects.values().filter(user=request.user))

        return render(request, 'service.html',{'services':services})

    if request.method == 'POST':
        # appointmentType = request.POST.get('appointmentType')
        name = request.POST.get('name')
        discription = request.POST.get('discription')
        user = request.POST.get('user')
        appointmentDate = request.POST.get('appointmentDate')
        time = request.POST.get('time')
        
        serviceupdate = Service()
        serviceupdate.appointmentDate = appointmentDate
        # serviceupdate.appointmentType = appointmentType
        serviceupdate.discription = discription
        serviceupdate.time = time
        serviceupdate.user = request.user
        serviceupdate.name = name
        serviceupdate.save()

        message = "Hello ,"+request.user.get_full_name()+" We are pleased to inform you that the Appointment for has been scheduled on "+str(appointmentDate)

        send_mail('Doctorz Appointment Scheduled', message, 'logickiddie@gmail.com', [request.user.email], fail_silently=False)

        ownermessage = "A new Bike service request has been booked by "+request.user.get_full_name()+" for  scheduled to be delivered on "+str(appointmentDate)
        send_mail('New Doctorz Appointment Booking', ownermessage, 'logickiddie@gmail.com', ['logickiddie@gmail.com'], fail_silently=False)


        services = list(Service.objects.values().filter(user=request.user))

        return render(request, 'service.html',{'services':services, 'success':'success'})

# def loginUser(request):
#     if request.method=="POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         #check if the user has entered the correct credentials
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect("/dashboard")
#     # A backend authenticated the credentials

#         else:
#             messages.success(request, 'Incorrect Credentials')
#             return render(request, 'login.html')
#     # No backend authenticated the credentials

#     return render(request, 'login.html')

# def logoutUser(request):
#     logout(request)
#     return redirect("/home")

# def signupUser(request):
#     if request.method=="POST":
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         firstname = request.POST.get('firstname')
#         lastname = request.POST.get('lastname')
#         user = User.objects.create_user(username, email, password)
#         user.first_name = firstname
#         user.last_name = lastname
#         user.save()
#     return render(request, 'signup.html')


    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     mobile = request.POST.get('mobile')
    #     query = request.POST.get('query')
    #     contact = Contact(name=name,email=email,mobile=mobile,query=query,date=datetime.today(),time=datetime.now().time())
    #     contact.save()
    #     messages.success(request, 'Your Query have been sent.')

    # return render(request, 'contact.html')