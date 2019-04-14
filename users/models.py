from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    institution = models.CharField(max_length=100, blank=False)
    subject_of_studies = models.CharField(max_length=100, blank=False)
    course_start_year = models.DateField(null=False, blank=False)
    course_end_year = models.DateField(null=False, blank=False)
    birth_date = models.DateField(null=True, blank=True)
    address_title = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    district = models.CharField(max_length=100, blank=True)
    address = models.TextField(max_length=500)