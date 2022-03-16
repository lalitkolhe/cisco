from django import forms  
from router.models import router_details  
class RouterForm(forms.ModelForm):  
    class Meta:  
        model = router_details  
        fields = "__all__"  