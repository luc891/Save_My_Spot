from django.db import models
from django.contrib.auth.models import AbstractUser

COUNTRIES = (
    ('FRANCE', 'France'),
    ('SWITZERLAND', 'Switzwerland'),
    ('GERMANY', 'Germany'),
    ('OTHER', 'Other')
)

LOCATIONS = (
    ('BASEL', 'lfsb'),
    ('DIJON', 'lfsd'),
    ('DÔLE', 'lfgj')
)

class User(AbstractUser):
    username = models.CharField(max_length=254, unique = True)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length = 24)
    adress = models.CharField(max_length=254, default = None, blank = True, null = True)
    country = models.CharField(max_length=12, choices=COUNTRIES, default = None, blank = True, null = True)
    is_club = models.BooleanField(default = False, blank = True, null = True)
    is_approach = models.BooleanField(default = False, blank = True, null = True)
    is_airport_man = models.BooleanField(default = False, blank = True, null = True)

    def __str__(self):
        return self.username
    
class Plane(models.Model):
    registration = models.CharField(max_length = 12)
    club = models.ForeignKey(User, on_delete = models.CASCADE)
    maker = models.CharField(max_length = 254)
    model = models.CharField(max_length = 254)

    def __str__(self):
        return self.username

class Airport(models.Model):
    icao_code = models.CharField(max_length = 4)
    approach_control = models.ForeignKey(User, default=None, on_delete=models.SET_DEFAULT)
    tower_control = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
class Calendar(models.Model):
    location = models.CharField(max_length=12, choices=LOCATIONS)
    event_type_slug = models.CharField(max_length=100)
    subscribers = models.ManyToManyField(User, related_name='subscribed_calendars', blank=True)
    is_airport_man = models.BooleanField(default=False)

class Reservation(models.Model):
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reserved_date = models.DateTimeField()
