from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from models import Club, Plane, Airport, Approach, Airport_manager

class ClubCreationForm(UserCreationForm):

    class Meta:
        model = Club

class ClubChangeForm(UserChangeForm):

    class Meta:
        model = Club

class PlaneCreationForm(UserCreationForm):

    class Meta:
        model = Plane

class PlaneChangeForm(UserChangeForm):

    class Meta:
        model = Plane

class AirportCreationForm(UserCreationForm):

    class Meta:
        model = Airport

class AirportChangeForm(UserChangeForm):

    class Meta:
        model = Airport

class AirportDGACCreationForm(UserCreationForm):

    class Meta:
        model = Approach

class AirportDGACChangeForm(UserChangeForm):

    class Meta:
        model = Approach

class AirportmanagerCreationForm(UserCreationForm):

    class Meta:
        model = Airport_manager

class AirportmanagerChangeForm(UserChangeForm):

    class Meta:
        model = Airport_manager


