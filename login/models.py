from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    picture = models.ImageField(default='profile_default.png',upload_to='users/')


class Games(models.Model):
    name = models.CharField(max_length=80,blank=False,null=False)
    year = models.IntegerField()
    prize = models.IntegerField()
    image = models.ImageField(upload_to='videogames/',blank=True,null=True)
    storage = models.IntegerField()
    score = models.IntegerField()
    platform = models.CharField(max_length=20,blank=False,null=False)
    E = 'EVERYONE'
    E10 = 'EVERYONE10'
    T = 'TEEN'
    M = 'MATURE'
    A = 'ADULT'
    RATING_CHOICES = [
        (E, 'E'),
        (E10, 'E+10'),
        (T, 'T'),
        (M, 'M'),
        (A, 'A'),
    ]
    rating = models.CharField(
        max_length=12,
        choices=RATING_CHOICES,
        default=E,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)