from django.contrib import admin
from .models import Service, ServiceDetail, Location, Entertainment
# Register your models here.
admin.site.register([Service, ServiceDetail, Location, Entertainment])