from rest_framework import serializers 
from .models import Locator

class LocatorSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Locator # tell django which model to use
        fields = ('id', 'name', 'price','image') # tell django which fields to include
