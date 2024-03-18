from django.contrib import admin
from django.urls import path
from uav.views import uavs, detail, rent,rent_an_uav, give_back, update, delete, add, rented


app_name = "uav"


urlpatterns = [
    path('', uavs, name = "uavs"),
    path("detail/<int:id>", detail, name = "detail"),
    path("rent/", rent, name = "rent"),
    path("rent-an-uav/<int:id>", rent_an_uav, name = "rent_an_uav"),
    path("give-back/<int:id>", give_back, name = "give_back"),
    path("update/<int:id>", update, name = "update"),
    path("delete/<int:id>", delete, name = "delete"),
    path("add/", add, name = "add"),    
    path("rented/", rented, name = "rented"),    
    
        
]