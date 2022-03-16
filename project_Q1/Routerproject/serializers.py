from .models import router_details
from rest_framework import serializers

class router_detailsserializer(serializers.ModelSerializer):
    class Meta:
        model = router_details
        fields ='__all__'
        
        
class router_detailserializers(serializers.ModelSerializer):
     class Meta:
         model = router_details
         fields =['Loopback']
    
