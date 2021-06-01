from django.contrib import admin

# Register your models here.
from .models import Service,Servicetype

admin.site.register(Service)
admin.site.register(Servicetype)