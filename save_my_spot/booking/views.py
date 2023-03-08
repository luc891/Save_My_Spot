from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

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
                new_object = Club.objects.create_user(form.cleaned_data['username'],
                                                      form.cleaned_data['email'],
                                                      form.cleaned_data['phone'],
                                                      form.cleaned_data['adress'],
                                                      form.cleaned_data['country'],
                                                      is_club = True)
            else:
                print(form.errors)
        elif choice == 'approach':
            form = ApproachCreationForm(request.POST)
            if form.is_valid():
                new_object = Approach.objects.create_user(form.cleaned_data['username'],
                                                          form.cleaned_data['email'],
                                                          form.cleaned_data['phone'],
                                                          is_approach = True)
            else:
                print(form.errors)
        else:
            form = AirportmanagerCreationForm(request.POST)
            if form.is_valid():
                new_object = Airport_manager.objects.create_user(form.cleaned_data['username'],
                                                                 form.cleaned_data['email'],
                                                                 form.cleaned_data['phone'],
                                                                 form.cleaned_data['adress'],
                                                                 is_airport_man = True)
            else:
                print(form.errors)
        new_object.save()
        return render(request, 'index.html')


def loginview(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        user = authenticate(username = request.POST['username'], password = request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("profil"))
        else:
            return render(request, 'login.html')

@login_required
def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def profil(request):
    ...