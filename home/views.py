from django.http import response
from django.shortcuts import render
from django.core.mail import send_mail
from .models import Servicetype, Service
import requests
from covid import Covid
import json


# Create your views here.
def index(request):
    response=requests.get('https://api.covid19api.com/total/dayone/country/india').json()
    return render(request, 'landingPage.html', {'response':response})

def dashboard(request):
    if request.method == 'GET':
        services = list(Servicetype.objects.values())
        return render(request, 'dashboard.html', {'services':services})

def profile(request):
    return render(request, 'profile.html')
    
def covid(request):
    response=requests.get('https://api.covid19api.com/total/dayone/country/india').json()
    # resp = response.json()
    # covid = Covid()
    # response = covid.get_status_by_country_name("india")
    # response = str(response)
    # response = json.dumps(response)
    return render(request, 'index.html', {'response':response})

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

        message = "Dear, "+request.user.get_full_name()+"\n Thank you for chosing DoctorZ, \n We are pleased to inform you that your Appointment has been scheduled on "+str(appointmentDate)+". \n DoctorZ"

        send_mail('Doctorz Appointment Scheduled', message, 'logickiddie@gmail.com', [request.user.email], fail_silently=False)

        ownermessage = "A new DoctorZ appointment request has been booked by "+request.user.get_full_name()+" for  scheduled to be delivered on "+str(appointmentDate)
        send_mail('New Doctorz Appointment Booking', ownermessage, 'logickiddie@gmail.com', ['logickiddie@gmail.com'], fail_silently=False)


        services = list(Service.objects.values().filter(user=request.user))

        return render(request, 'service.html',{'services':services, 'success':'success'})
