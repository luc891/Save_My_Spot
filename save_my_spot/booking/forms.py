from django import forms
from .models import Airport, Plane

class PlaneForm(forms.Form):

    class Meta:
        model = Plane
        fields = ['registration', 'club', 'maker', 'model']

class AirportForm(forms.Form):

    class Meta:
        model = Airport
        fields = ['icao_code', 'approach_control', 'tower_control']

