from rest_framework import serializers
from . import models

class RoadSignTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RoadSignType
        fields = '__all__'

class RoadSignSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RoadSign
        fields = '__all__'