from django.contrib.auth.models import User
from django.db import models


class Userprofile(models.Model):
    user = models.OneToOneField(User, verbose_name="userprofile", on_delete=models.CASCADE)
    is_vendor = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.username