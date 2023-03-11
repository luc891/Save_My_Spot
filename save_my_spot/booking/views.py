from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password

from .models import User, COUNTRIES
from .functions import matching_password

# Landing view
def index(request):
    return render(request, 'index.html')

# Create account view
def register(request):
    if request.method == 'GET':
        choice = COUNTRIES
        return render(request, 'register.html', {
                       'choice' : choice
                    })
    else:             
        user = User.objects.create_user(username = request.POST['username'],
                                        email = request.POST['email'],
                                        phone = request.POST['phone'],
                                        adress = request.POST['adress'],
                                        country = request.POST['country'])
        
        choice = request.POST['account_type'] 
        if choice == 'club':
            user.is_club = True
        elif choice == 'approach':
            user.is_approach = True
        else:
            user.is_airport_man = True
        
        if (result := matching_password(request.POST)) == True:
            user.set_password(request.POST['password2'])

            user.save()
            login(request, user) 
            return render(request, 'profil.html')
        
        else:
            user.delete()
            return render(request, 'register.html',{
                'error': result
            })


def loginview(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        user = authenticate(username = request.POST['username'], password = request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("profil"))
        else:
            return render(request, 'login.html', {
                'message' : 'Invalid credentials'
            })

@login_required
def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def profil(request):
    return render(request, 'profil.html')