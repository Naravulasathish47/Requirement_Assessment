from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=200)
    UserName = models.CharField(max_length=200)
    Date_of_Birth = models.DateTimeField("date published")
    Address = models.CharField(max_length=2000)
    Phone = models.IntegerField(max_length=13)
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.user.username} Profile'

