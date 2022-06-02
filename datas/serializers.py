from dataclasses import fields
import imp
from pyexpat import model
from rest_framework import serializers
from .models import *

class PackageSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Packages
        fields='__all__'



class TrekGuideSerailizer(serializers.ModelSerializer):
    class Meta:
        model=TrekGuides
        fields='__all__'


class TransportationSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Transportation
        fields='__all__'


class AccomodationSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Accomodation
        fields='__all__'



class DestiTransportationSerailizer(serializers.ModelSerializer):
    class Meta:
        model=DestinationTransportation
        fields='__all__'

class DestinationSerailizer(serializers.ModelSerializer):
    accomodations=serializers.SerializerMethodField()
    transportations=serializers.SerializerMethodField()
    class Meta:
        model=Destination
        fields='__all__'
    def get_accomodations(self,object):
        return AccomodationSerailizer(object.accomodations.all(),many=True).data

    def get_transportations(self,object):
        return TransportationSerailizer(object.transportations.all(),many=True).data