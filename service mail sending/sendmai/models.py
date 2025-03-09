from django.db import models

# Create your models here.
class mail(models.Model):
    name = models.CharField(max_length=1000,blank=True)
    company_name = models.CharField(max_length=1000,blank=True)
    position = models.CharField(max_length=1000,blank=True)
    mail = models.CharField(max_length=1000,blank=True)
    phone_number = models.CharField(max_length=1000,blank=True)
    service_type = models.CharField(max_length=1000,blank=True)
    country = models.CharField(max_length=1000,blank=True)
    state = models.CharField(max_length=1000,blank=True)
    city = models.CharField(max_length=1000,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=10000,blank=True)

