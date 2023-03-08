from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from .forms import ClubCreationForm, ApproachCreationForm, AirportmanagerCreationForm
from .models import Club, Approach, Airport_manager

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        choice = request.POST['account_type']
        if choice == 'club':
            form = ClubCreationForm(request.POST)
            if form.is_valid():
                new_object = Club(form.cleaned_data)
        elif choice == 'approach':
            form = ApproachCreationForm(request.POST)
            if form.is_valid():
                new_object = Approach(form.cleaned_data)
        else:
            form = AirportmanagerCreationForm(request.POST)
            if form.is_valid():
                new_object = Airport_manager(form.cleaned_data)

        new_object.save()
        return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')
