from dataclasses import fields
import imp
from pyexpat import model
from rest_framework import serializers
from .models import *

class PackageSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Packages
        fields=['id','package_name','package_price','package_provider','package_days','package_description','package_image']



class TrekGuideSerailizer(serializers.ModelSerializer):
    class Meta:
        model=TrekGuides
        fields='__all__'