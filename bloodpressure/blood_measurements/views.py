from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .models import Measurements
from rest_framework import viewsets, permissions
from .serializers import MeasurementSerializer


from django.shortcuts import render

from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class MeasurementViewSets(viewsets.ModelViewSet):
        queryset = Measurements.objects.all()
        serializer_class = MeasurementSerializer
        