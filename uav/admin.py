from django.contrib import admin
from .models import UAV, RentedUAVs

# Register your models here
# 

admin.site.register(RentedUAVs)


@admin.register(UAV)

class UAVAdmin(admin.ModelAdmin):

    list_display = ["model_name", "manufacturer","uav_type", "weight"]
    list_display_links = ["model_name"]
    search_fields = ["model_name"]
    list_filter = ["manufacturer"]

    class Meta:
        model = UAV
