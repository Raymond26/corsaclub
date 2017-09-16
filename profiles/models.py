from django.db import models

class UserProfile(models.Model):

    def __str__(self):
        return self.user.username