""" Profile Model """

# Django.
from django.db import models

# Utilities
from productive.utils.models import ProduModel


# Create your models here.

class Profile(ProduModel):
    """ Modelo de perfil del usuario. 
    Perfil publico de cada usuario. """

    user = models.OneToOneField('user.User',related_name="profile", on_delete=models.CASCADE)

    picture = models.ImageField(
        'profile picture', 
        upload_to = 'user/pictures/',
        blank = True,
        null = True,
        )

    polls = models.IntegerField(default=0) 

    def __str__(self):
        return str(self.user)