from django.http import response
from django.shortcuts import render
from django.core.mail import send_mail
from requests import sessions
from requests.sessions import session
from .models import Servicetype, Service
import requests
from datetime import date
import json


# Create your views here.
def index(request):
    response=requests.get('https://api.covid19api.com/total/dayone/country/india').json()
    # url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india_timeline"

    # headers = {
    #     'x-rapidapi-key': "3b73f69c98msh63f861f599d3f0fp18a3d6jsn6262635c444f",
    #     'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
    #      }

    # response = requests.request("GET", url, headers=headers).json()

    return render(request, 'landingPage.html', {'response':response})

def dashboard(request):
    if request.method == 'GET':
        services = list(Servicetype.objects.values())
        return render(request, 'dashboard.html', {'services':services})

def profile(request):
    return render(request, 'profile.html')


def vaccine(request):
    try:
        today = date.today()
        d1 = today.strftime("%d-%m-%Y")
        
        pincode = request.GET.get('pincode')
        pincode = str(pincode)
        # pincode = '110065'
#         baseurl = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=110019&date=11-07-2021'
        baseurl = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}'.format(pincode,d1)
        
        # pinURL = baseurl + pincodeU + '&date='
        # apiURL = pinURL + d1
        vaccine = requests.get(baseurl)
        data = vaccine.json()
        vaccinedata = data["sessions"]
        return render(request, 'vaccine_data.html', {'vaccinedata':vaccinedata})

    except:
        return render(request, 'vaccine_data.html')

# def vaccineBook(request):
#     today = date.today()
#     d1 = today.strftime("%d-%m-%Y")
#     pincodeU = '110046'
#     baseurl = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}'.format(pincodeU,d1)
#     # pincode = request.POST.get('pincode')
#     # pincodeU = str(pincode)
#     # pinURL = baseurl + pincodeU + '&date='
#     # apiURL = pinURL + d1
#     vaccine = requests.get(baseurl)
#     # print(vaccinedate)
#     data = vaccine.json()
#     vaccinedata = data["sessions"]
#     # vaccinedata = data.values()
#     return render(request, 'vaccine_data.html',{'vaccinedata':vaccinedata})
    
def covid(request):
    response=requests.get('https://api.covid19api.com/total/dayone/country/india').json()
    # url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india_timeline"

    # headers = {
    #     'x-rapidapi-key': "3b73f69c98msh63f861f599d3f0fp18a3d6jsn6262635c444f",
    #     'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
    #      }

    # respon = requests.request("GET", url, headers=headers).json()
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

        message = "Dear, "+request.user.get_full_name()+"\n Thank you for chosing DoctorZ, \n We are pleased to inform you that your Appointment has been scheduled on "+str(appointmentDate)+" at "+ str(time)+".\n Your Description: "+ discription +" \n DoctorZ"

        send_mail('Doctorz Appointment Scheduled', message, 'logickiddie@gmail.com', [request.user.email], fail_silently=False)

        ownermessage = "A new DoctorZ appointment request has been booked by "+request.user.get_full_name()+" and scheduled to be delivered on "+str(appointmentDate)+" at "+ str(time)+".\n Patient Discription:"+ discription
        send_mail('New Doctorz Appointment Booking', ownermessage, 'logickiddie@gmail.com', ['logickiddie@gmail.com'], fail_silently=False)


        services = list(Service.objects.values().filter(user=request.user))

        return render(request, 'service.html',{'services':services, 'success':'success'})
