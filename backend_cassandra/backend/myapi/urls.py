from django.conf.urls import url
from myapi.views import *
from django.urls import path
urlpatterns = [
    path('getUser/<str:username>/',getUser),
    path('getPerson/<str:username>/',getPerson),
    path('createTablePerson',createTablePerson),
    path('writePersons',writePersons),
    
]