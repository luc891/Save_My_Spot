from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Club, Plane, Airport, Approach, Airport_manager

class ClubCreationForm(UserCreationForm):
    
    class Meta:
        model = Club
        fields = ['username', 'email', 'phone', 'adress', 'country']

class ClubChangeForm(UserChangeForm):

    class Meta:
        model = Club
        fields = ['username', 'email', 'phone', 'adress', 'country']

class PlaneCreationForm(UserCreationForm):

    class Meta:
        model = Plane
        fields = ['registration', 'club', 'maker', 'model']

class PlaneChangeForm(UserChangeForm):

    class Meta:
        model = Plane
        fields = ['registration', 'club', 'maker', 'model']

class AirportCreationForm(UserCreationForm):

    class Meta:
        model = Airport
        fields = ['icao_code', 'approach_control', 'tower_control']

class AirportChangeForm(UserChangeForm):

    class Meta:
        model = Airport
        fields = ['icao_code', 'approach_control', 'tower_control']

class ApproachCreationForm(UserCreationForm):

    class Meta:
        model = Approach
        fields = ['username', 'email', 'phone']

class ApproachChangeForm(UserChangeForm):

    class Meta:
        model = Approach
        fields = ['username', 'email', 'phone']

class AirportmanagerCreationForm(UserCreationForm):

    class Meta:
        model = Airport_manager
        fields = ['username', 'email', 'phone', 'adress']

class AirportmanagerChangeForm(UserChangeForm):

    class Meta:
        model = Airport_manager
        fields = ['username', 'email', 'phone', 'adress']


