from pyexpat import model
from rest_framework import serializers
from ..datas.models import Accomodation

class AccomodationSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Accomodation
        fields=['id','accomodation_name','accomodation_price','accomodation_contact','accomodation_location','accomodation_description','accomodation_image']



