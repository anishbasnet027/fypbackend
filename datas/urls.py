
from django.urls import path
from .views import *

urlpatterns = [
    path('login/',AuthView.as_view()),
    path('register/',RegisterView.as_view()),
    path('packages/',PackageView.as_view()),
      path('guides/',TrekGuideView.as_view()),
]
