
from django.urls import path
from .views import *

urlpatterns = [
    path('login/',AuthView.as_view()),
    path('register/',RegisterView.as_view()),
    path('packages/',PackageView.as_view()),
    path('trekguides/',TrekGuideView.as_view()),
    path('destination/',PackageView.as_view()),
    path('transportation/',TrekGuideView.as_view()),
    path('accomodation/',TrekGuideView.as_view()),
]

