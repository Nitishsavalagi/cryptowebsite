from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Favorites(models.Model):
    Name = models.CharField(max_length=250)
    Symbol = models.CharField(max_length=250)
    Current_Price = models.CharField(max_length=200)

    def __str__(self):
        return self.Name + self.Current_Price




class UserInfo(models.Model):

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username
