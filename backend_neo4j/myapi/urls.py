from django.conf.urls import url
from myapi.views import *
from django.urls import path
urlpatterns = [
    #path('person',personDetails),
    path('getAllPersons',getAllPersons),
    #path('city',cityDetails),
    #path('getAllCities',getAllCities),
    #path('connectPaC',connectPaC),
    #path('connectPaP',connectPaP),
    #path('users/<str:username>/',getUser),
    #path('usersdata',writeUser),
    #path('getAllUsers',getAllUsers),
    #path('deleteAllUsers',deleteAllUsers),
    path('writePersons',writePersons),
    path('deletePersons',deletePersons),
    path('writeBankAccounts',writeBankAccounts),
    path('deleteBankAccounts',deleteBankAccounts),
    path('createPersonsOwns',createPersonsOwns),
    
]

