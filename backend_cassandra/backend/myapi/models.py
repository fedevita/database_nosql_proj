from django.db import models

class User(models.Model):
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)

class Person(models.Model):
    id = models.CharField(max_length = 1000, primary_key=True)
    first_name = models.CharField(max_length = 1000)
    last_name = models.CharField(max_length = 1000)
    email = models.CharField(max_length = 1000)
    gender =  models.CharField(max_length = 1000)
    address = models.CharField(max_length = 1000)
    phone = models.CharField(max_length = 1000)
    country =  models.CharField(max_length = 1000)
    country_code = models.CharField(max_length = 1000)
    bank_id = models.CharField(max_length = 1000)
    is_pep = models.PositiveSmallIntegerField() 
    password = models.CharField(max_length = 1000)