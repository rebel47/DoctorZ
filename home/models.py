from django.db import models
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse

# User Model
# class Users(models.Model):
#     username = models.CharField(max_length=122)
#     email =  models.CharField(max_length=122)
#     password =  models.CharField(max_length=122)
#     firstname =  models.CharField(max_length=122)
#     lastname =  models.CharField(max_length=122)


    

# Service Model
class Service(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    time = models.TimeField()

    appointmentDate = models.DateField()

    discription = models.TextField(max_length=255, blank=True)

    appointmentType = models.TextField(max_length=100, blank=True)

    status = models.TextField(max_length=30, default="Scheduled")

    completed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):

        if self.completed == False:
            super(Service, self).save(*args, **kwargs)

        else:
            # Make sure less secure app is ON on the google accounnt
            message = "Dear "+self.user.get_full_name()+", Thank you for chosing DoctorZ, we hope you like our services. \n Have a good Health \n DoctorZ"
            send_mail('DoctorZ Appointment Completed', message, 'logickiddie@gmail.com', [self.user.email], fail_silently=False)
            super(Service, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.appointmentType + " " + self.user.get_full_name()}'
    


       


class Servicetype(models.Model):

    name = models.TextField(max_length=30, blank=True)

    description = models.TextField(max_length=255, blank=True)

    onhold = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'