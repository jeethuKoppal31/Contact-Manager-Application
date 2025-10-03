from django.db import models

class Contact(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    address = models.TextField()  
    email = models.EmailField(unique=False) 
    phone = models.CharField(max_length=15, unique=False)