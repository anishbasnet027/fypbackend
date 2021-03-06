from django.urls import path
from .views import *

urlpatterns = [
    path('login/',AuthView.as_view()),
    path('register/',RegisterView.as_view()),
    path('packages/',PackageView.as_view()),
    path('trekguides/',TrekGuideView.as_view()),
    path('destination/',DestinationView.as_view()),
    path('transportation/',TransportationView.as_view()),
    path('accomodation/',AccomodationView.as_view()),
    path('destinationtransportation/',DestiTransportationView.as_view()),
    path('destinationaccomodation/',DestiAccomodationView.as_view()),
]

