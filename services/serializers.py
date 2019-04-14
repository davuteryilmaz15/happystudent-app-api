from rest_framework import serializers
from .models import Service, ServiceDetail, Location, Entertainment

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class ServiceDetailSerializer(serializers.ModelSerializer):
    service = serializers.SlugRelatedField(queryset=Service.objects.all(), slug_field='name')
    locations = serializers.JSONField(source='get_locations')
    class Meta:
        model = ServiceDetail
        fields = ('service', 'info', 'check_list', 'form_url', 'locations')
        read_only_fields = (
            'locations',
        )

class EntertainmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entertainment
        fields = '__all__'
    