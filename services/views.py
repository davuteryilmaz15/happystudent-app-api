from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .serializers import ServiceSerializer, ServiceDetailSerializer, EntertainmentSerializer
from .models import Service, ServiceDetail, Entertainment
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.

class ServiceList(generics.ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = ()
    queryset = Service.objects.all().order_by('priority')
    serializer_class = ServiceSerializer

class ServiceDetailList(generics.ListAPIView):
    def get_queryset(self):
        self.service = get_object_or_404(Service, name=self.kwargs['service_name'])
        return ServiceDetail.objects.filter(service=self.service)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = ()
    serializer_class = ServiceDetailSerializer

class EntertainmentList(generics.ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = ()
    queryset = Entertainment.objects.all()
    serializer_class = EntertainmentSerializer