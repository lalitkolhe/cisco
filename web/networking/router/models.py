from django.db import models

# Create your models here.
class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)  
    class Meta:  
        db_table = "employee"
		
from django.db import models

# Create your models here.
class router_details(models.Model):  
    Sapid = models.CharField(max_length=18)  
    Hostname = models.CharField(max_length=14)  
    Loopback=models.GenericIPAddressField()
    Macaddress = models.CharField(max_length=17)  
    class Meta:  
        db_table = "router_details"
		
