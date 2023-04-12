from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password

from .models import User, COUNTRIES, LOCATIONS, Calendar, Reservation
from .functions import matching_password, get_password_error_message


# Landing view
def index(request):
    locations = LOCATIONS
    return render(request, 'index.html', {
                  'locations' : locations
                  })

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
            error_message = get_password_error_message(result)
            return render(request, 'register.html',{
                'error': error_message
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

@login_required
def profil(request):
    return render(request, 'profil.html')

@login_required
def subscribe_calendar(request, calendar_id):
    # Récupérer le calendrier en fonction de l'ID passé en paramètre
    calendar = Calendar.objects.get(id=calendar_id)

    # Vérifier si l'utilisateur est un club
    if request.user.is_club:
        # Ajouter l'utilisateur à la liste des abonnés du calendrier
        calendar.subscribers.add(request.user)
        calendar.save()
        return redirect('calendars:calendar_detail', calendar_id=calendar_id)
    else:
        # Rediriger vers une page d'erreur ou afficher un message d'erreur approprié
        pass

@login_required
def view_reservations(request):
    # Récupérer toutes les réservations associées à l'utilisateur connecté
    reservations = Reservation.objects.filter(user=request.user)

    # Afficher les réservations dans le template
    return render(request, 'reservations.html', {'reservations': reservations})

@login_required
def cancel_reservation(request, reservation_id):
    # Récupérer la réservation en fonction de l'ID passé en paramètre
    reservation = Reservation.objects.get(id=reservation_id)

    # Vérifier si l'utilisateur est un utilisateur avec is_approach vrai
    if request.user.is_approach:
        # Supprimer la réservation
        reservation.delete()
        return redirect('calendars:view_reservations')
    else:
        # Rediriger vers une page d'erreur ou afficher un message d'erreur approprié
        pass

@login_required
def edit_reservation(request, reservation_id):
    # Récupérer la réservation en fonction de l'ID passé en paramètre
    reservation = Reservation.objects.get(id=reservation_id)

    # Vérifier si l'utilisateur est un utilisateur avec is_airport_man vrai
    if request.user.is_airport_man:
        if request.method == 'POST':
            # Récupérer les nouvelles informations de réservation à partir du formulaire POST
            new_reserved_date = request.POST['reserved_date']

            # Modifier la réservation avec les nouvelles informations
            reservation.reserved_date = new_reserved_date
            reservation.save()

            # Rediriger vers la liste des réservations ou afficher un message de succès
            return redirect('calendars:view_reservations')
        else:
            # Afficher le formulaire de modification de réservation dans le template
            return render(request, 'edit_reservation.html', {'reservation': reservation})
    else:
        # Rediriger vers une page d'erreur ou afficher un message d'erreur approprié
        pass
