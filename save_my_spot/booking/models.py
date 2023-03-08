from django.db import models
from django.contrib.auth.models import AbstractUser

COUNTRIES = (
    ('FRANCE', 'France'),
    ('SWITZERLAND', 'Switzwerland'),
    ('GERMANY', 'Germany'),
    ('OTHER', 'Other')
)

class User(AbstractUser):
    username = models.CharField(max_length = 254, unique = True)
    email = models.EmailField(max_length = 254)
    phone = models.CharField(max_length = 24)


    def __str__(self):
        return self.username

class Club(User):
    adress = models.CharField(max_length=254)
    country = models.CharField(max_length=12, choices=COUNTRIES, default = 'FRANCE')

    def __str__(self):
        return self.username

class Approach(User):

    def __str__(self):
        return self.username

class Airport_manager(User):
    adress = models.CharField(max_length=254)

    def __str__(self):
        return self.username
    
class Plane(models.Model):
    registration = models.CharField(max_length = 12)
    club = models.ForeignKey('Club', on_delete = models.CASCADE)
    maker = models.CharField(max_length = 254)
    model = models.CharField(max_length = 254)

    def __str__(self):
        return self.username

class Airport(models.Model):
    icao_code = models.CharField(max_length = 4)
    approach_control = models.ForeignKey('Approach', default=None, on_delete=models.SET_DEFAULT)
    tower_control = models.BooleanField(default=False)

    def __str__(self):
        return self.username