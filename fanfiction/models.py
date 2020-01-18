from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_dark = models.BooleanField(default=False)

    def swith_theme(self):
        self.is_dark = not self.is_dark
