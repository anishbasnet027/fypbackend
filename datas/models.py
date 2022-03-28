from django.db import models
from django.contrib.auth.models import AbstractUser

class Packages(models.Model): #for packages
    package_name=models.CharField(max_length=40,blank=False)
    package_price=models.IntegerField(max_length=6,blank=False)
    package_provider=models.CharField(max_length=100, blank=False)
    package_days=models.IntegerField(max_length=2, blank=False)
    package_description=models.CharField(max_length=100,blank=True)
    package_image=models.ImageField(upload_to='images',blank=False)

    def __str__(self):
        return self.package_name

class TrekGuides(models.Model): #for trek guides
    guide_fullName=models.CharField(max_length=40,blank=False)
    guide_contact=models.IntegerField(max_length=10,blank=False)
    guide_email=models.EmailField(max_length=100, blank=False)
    guide_experience=models.IntegerField(max_length=2, blank=False)
    guide_description=models.CharField(max_length=100,blank=True)
    guide_perDay_price=models.IntegerField(max_length=4, blank=False)
    guide_image=models.ImageField(upload_to='images',blank=False)

    def __str__(self):
        return self.package_name

class Destination(models.Model): #for destination
    destination_choices=[('T','Treking'),('H','Hiking')]
    destination_type=models.CharField(max_length=1, choices=destination_choices, blank=False)
    destination_name=models.CharField(max_length=100,blank=True)
    destination_location=models.CharField(max_length=100,blank=True)
    destination_altitude=models.IntegerField(max_length=4, blank=False)
    destination_distance=models.IntegerField(max_length=4, blank=False)
    destination_avgPrice=models.IntegerField(max_length=6, blank=False)
    destination_equipment=models.CharField(max_length=4, blank=False)
    destination_emergencyContact=models.IntegerField(max_length=10, blank=False)
    destination_emergencyDetail=models.CharField(max_length=100,blank=True)
    destination_season=models.CharField(max_length=100,blank=True)
    destination_medicalNeeds=models.CharField(max_length=100,blank=True)
    destination_scams=models.CharField(max_length=100,blank=True)
    destination_image=models.ImageField(upload_to='images',blank=False)

    def __str__(self):
        return self.destination_name

class Transportation(models.Model):
    destination_id=models.ForeignKey(Destination, on_delete=models.CASCADE)
    transportation_name=models.CharField(max_length=100,blank=True)
    transportation_price=models.IntegerField(max_length=4, blank=False)
    transportation_contact=models.IntegerField(max_length=10, blank=False)
    transportation_location=models.CharField(max_length=100,blank=True)
    transportation_description=models.CharField(max_length=100,blank=True)
    transportation_image=models.ImageField(upload_to='images',blank=False)
    def __str__(self):
        return self.transportation_name

class Accomodation(models.Model):
    destination_id=models.ForeignKey(Destination, on_delete=models.CASCADE)
    accomodation_name=models.CharField(max_length=100,blank=True)
    accomodation_price=models.IntegerField(max_length=4, blank=False)
    accomodation_contact=models.IntegerField(max_length=10, blank=False)
    accomodation_location=models.CharField(max_length=100,blank=True)
    accomodation_description=models.CharField(max_length=100,blank=True)
    accomodation_image=models.ImageField(upload_to='images',blank=False)
    def __str__(self):
        return self.accomodation_name
