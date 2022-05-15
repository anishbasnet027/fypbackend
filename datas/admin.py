from django.contrib import admin

# Register your models here.
from typing import List
from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Packages)
class admin_package(admin.ModelAdmin):
    List_display = ['First Name', 'Last Name', 'Email Address']

@admin.register(TrekGuides)
class admin_trekGuides(admin.ModelAdmin):
    List_display = ['First Name', 'Last Name', 'Email Address']

@admin.register(Destination)
class admin_destination(admin.ModelAdmin):
    List_display = ['First Name', 'Last Name', 'Email Address']

@admin.register(Transportation)
class admin_transportation(admin.ModelAdmin):
    List_display = ['First Name', 'Last Name', 'Email Address']

@admin.register(Accomodation)
class admin_accomodation(admin.ModelAdmin):
    List_display = ['First Name', 'Last Name', 'Email Address']


@admin.register(DestinationTransportation)
class admin_DestinationTransportation(admin.ModelAdmin):
    List_display = ['First Name', 'Last Name', 'Email Address']