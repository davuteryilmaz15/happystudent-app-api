from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, verbose_name='Servis Adı')
    priority = models.SmallIntegerField(verbose_name='Öncelik')
    title = models.CharField(max_length=50, verbose_name='Başlık')
    image_url = models.CharField(max_length=255, blank=True, null=True)
    coupon_code = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title

class Location(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='locations')
    longitude = models.CharField(max_length=21, blank=True, null=True)
    latitude = models.CharField(max_length=21, blank=True, null=True)

class ServiceDetail(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='details')
    info = models.CharField(max_length=100, verbose_name='Bilgi')
    check_list = models.TextField(max_length=1000, verbose_name='Check List')
    form_url = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.info
    
    def get_locations(self):
        locations = list()
        for location in Location.objects.filter(service=self.service):
            locations.append({'longitude':location.longitude, 'latitude':location.latitude})
        return locations

class Entertainment(models.Model):
    name = models.CharField(max_length=50, verbose_name='İsim')
    info = models.CharField(max_length=50, verbose_name='İnfo')
    image_url = models.CharField(max_length=255, verbose_name='Fotoğraf')
    latitude = models.CharField(max_length=21, verbose_name='Enlem')
    longitude = models.CharField(max_length=21, verbose_name='Boylam')
    coupon_code = models.CharField(max_length=50, verbose_name='Kupon Kodu')
    status = models.BooleanField(default=True, verbose_name='Durum')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name