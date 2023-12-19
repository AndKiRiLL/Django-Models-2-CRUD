from django.db import models

class User(models.Model):

    email    = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    login    = models.CharField(max_length=25)

    def __str__(self):
        return self.login
