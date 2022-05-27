from tkinter import E
from urllib import response
from django.shortcuts import render
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *

# Create your views here.
def get_tokens_for_user(user):
    """
    Get Acess and Refresh for specified User
    """
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class AuthView(APIView):
    """
    Extends APIView that handles authorization and login for all Users.
    """
    permission_classes = (AllowAny,)

    # Post Request for Login

    def post(self, request):
        '''
        login post req
        '''
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        user = authenticate(username=username, password=password)

        if user:
            cookie = get_tokens_for_user(user)['access']
            return Response ({'access_token':cookie, 'first_name':user.first_name, 'last_name':user.last_name,'email':user.email, 'username':user.username  })
        else:
            return Response("Wrong username/ password found")

       

User = get_user_model()
class RegisterView(APIView):
    def post(self, request):
        password = request.data.get('password', '')
        data = {
            'first_name': request.data.get('first_name', ''),
            'last_name': request.data.get('last_name', ''),
            'username': request.data.get('username', ''),
            'email': request.data.get('email', '')
        }
        try:
            user=User.objects.create(**data)
            user.set_password(password)
            user.save()
            return Response("Registration sucessfull")
        except Exception as e:
            return Response("The username or email is already used")
from rest_framework.parsers import MultiPartParser
    

# for packages
class PackageView(APIView):
    def get(self, request):
        serializer = PackageSerailizer(Packages.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TrekGuideView(APIView):
    parser_classes = (MultiPartParser,)
    def get(self, request):
        serializer = TrekGuideSerailizer(TrekGuides.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=TrekGuideSerailizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class DestinationView(APIView):
    def get(self, request):
        serializer = DestinationSerailizer(Destination.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TransportationView(APIView):
    def get(self, request):
        serializer = TransportationSerailizer(Transportation.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AccomodationView(APIView):
    def get(self, request):
        serializer = AccomodationSerailizer(Accomodation.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DestiTransportationView(APIView):
    def get(self, request):
        serializer = DestiTransportationSerailizer(DestinationTransportation.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DestiAccomodationView(APIView):
    def get(self, request):
        serializer = DestiAccomodationSerailizer(DestinationAccomodation.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

'''sawedae awed eawda awdd cawcaesssssssssssssssssssssssssssssssssssssssssssssssssss'''

'''sawedae awed eawda awdd cawcaesssssssssssssssssssssssssssssssssssssssssssssssssss'''

'''sawedae awed eawda awdd cawcaesssssssssssssssssssssssssssssssssssssssssssssssssss'''

'''sawedae awed eawda awdd cawcaesssssssssssssssssssssssssssssssssssssssssssssssssss'''

'''sawedae awed eawda awdd cawcaesssssssssssssssssssssssssssssssssssssssssssssssssss'''
