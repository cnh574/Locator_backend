from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import LocatorSerializer
from .models import Locator

class LocatorList(generics.ListCreateAPIView):
    queryset = Locator.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = LocatorSerializer # tell django what serializer to use

class LocatorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Locator.objects.all().order_by('id')
    serializer_class = LocatorSerializer
