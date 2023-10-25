from django.shortcuts import render
from rest_framework import generics
from .models import emissions
from .serializers import emissionsSerializer

class emissionsListCreate(generics.ListCreateAPIView):
    queryset = emissions.objects.all()
    serializer_class = emissionsSerializer
