from rest_framework import serializers
from .models import RoadSignType

class RoadSignTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RoadSignType
        fields = ('name', 'description')