from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.loginview, name='login'),
    path('logout', views.logoutview, name='logout'),
    path('register', views.register, name='register'),
    path('profil', views.profil, name='profil')
]