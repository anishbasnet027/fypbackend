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
        Post request for logging in a User
        '''
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        user = authenticate(username=username, password=password)

        if user:
            cookie = get_tokens_for_user(user)['access']
            return Response ({'access_token':cookie})
        else:
            return Response("invalid")

       

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

        user=User.objects.create(**data)
        user.set_password(password)
        user.save()
        return Response("sucessfull")

# for packages
class PackageView(APIView):
    def get(self,request):
        package=Packages.objects.all()
        print('package')
        serializers=PackageSerailizer(package,many=True)
        return JsonResponse(serializers.data,safe=False)

        # elif request.method=='POST':
        #     data = JSONParser().parse(request)
        #     serializers=PackageSerailizer(data=data)

        #     if serializers.is_valid():
        #         serializers.save
        #         return JsonResponse(serializers.data,status=201)
        #     return JsonResponse(serializers.errors,status=400)

# class TrekGuideView(APIView):
#     def get(self,request):
#         trekguide=TrekGuides.objects.all()
#         print('package')
#         serializers=TrekGuideSerailizer(trekguide,many=True)
#         return JsonResponse(serializers.data,safe=False)

class TrekGuideView(APIView):
    def get(self, request):
        serializer = TrekGuideSerailizer(TrekGuides.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)