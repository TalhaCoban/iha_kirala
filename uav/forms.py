from django import forms
from uav.models import UAV, RentedUAVs


class UAVForm(forms.ModelForm):
    class Meta:
            model = UAV
            fields = [
                "model_name",
                "manufacturer",
                "uav_type",
                "weight",
                "dimensions_length",
                "dimensions_width",
                "dimensions_height",
                "max_speed",
                "range",
                "endurance",
                "payload_capacity",
                "communication_range",
                "navigation_system",
                "camera_imaging_system",
                "operating_altitude",
                "takeoff_landing_method",
                "control_interface",
                "special_features",
                "rent_price_per_hour"
            ]
            
            
class RentedUAVsForm(forms.ModelForm):
    class Meta:
            model = RentedUAVs  
            fields = [
                "startdate",
                "enddate"
            ]
            widgets = {
                'startdate': forms.DateInput(attrs={'type': 'date'}),
                'enddate': forms.DateInput(attrs={'type': 'date'})
            }