from django.db import models
from macaddress.fields import MACAddressField

# Create your models here.
class router_details(models.Model):
    Sapid=models.IntegerField()
    Hostname=models.CharField(max_length=14)
    Loopback=models.GenericIPAddressField()
    Macaddress=MACAddressField(null=True, blank=True)
    
