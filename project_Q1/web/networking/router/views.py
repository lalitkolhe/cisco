from django.shortcuts import render, redirect  
from router.forms import RouterForm  
from router.models import router_details  
import requests, json
# Create your views here.  
def router(request):  
    if request.method == "POST":  
        form = RouterForm(request.POST)  
        if form.is_valid():  
            print(type(request.POST))
            print(request.POST)
            try:  
                _data = {
                    "Sapid": form.get("Sapid"),
                    "Hostname": form.get("Hostname"),
                    "Loopback": form.get("Loopback"),
                    "Macaddress": form.get("Macaddress")
                }
                requests.post('localhost',data=json.dumps(_data))
                
                #form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = RouterForm()  
        return render(request,'index.html',{'form':form})  
def show(request):  
    routers = router_details.objects.all()  
    return render(request,"show.html",{'routers':routers})  
def edit(request, id):  
    router = router_details.objects.get(id=id)  
    return render(request,'edit.html', {'router':router})  
def update(request, id):  
    router = router_details.objects.get(id=id)  
    form = RouterForm(request.POST, instance = router)  
    if form.is_valid():  
        _data = {
            "Sapid": form.get("Sapid"),
            "Hostname": form.get("Hostname"),
            "Loopback": form.get("Loopback"),
            "Macaddress": form.get("Macaddress")
        }
        _api = 'localhost/router/' + str(id)
        requests.post(_api,data=json.dumps(_data))
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'router': router})  
def destroy(request, id):  
    router = router_details.objects.get(id=id)  
    router.delete()  
    return redirect("/show")  