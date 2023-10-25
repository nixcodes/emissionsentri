from rest_framework import serializers
from .models import emissions

class emissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = emissions
        fields = '__all__'
