from django.urls import path
from . import views

app_name = 'services'
urlpatterns = [
    path('', views.ServiceList.as_view(), name="service_list"),
    path('entertainments/', views.EntertainmentList.as_view(), name="entertainment_list"),
    path('<str:service_name>/', views.ServiceDetailList.as_view(), name="service_detail_list"),
    
]