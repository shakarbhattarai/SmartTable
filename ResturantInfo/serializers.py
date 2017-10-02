from rest_framework import serializers
from ResturantInfo.models import ResturantInfo, LANGUAGE_CHOICES, STYLE_CHOICES

class ResturantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResturantInfo
        fields = ('id','CreatedAt', 'ResturantName', 'OwnerName', 'District', 'Address', 'Trial')

