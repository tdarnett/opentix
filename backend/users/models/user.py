from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django_extensions.db.models import TimeStampedModel


class User(AbstractBaseUser, TimeStampedModel):
    first_name = models.CharField(max_length=32, blank=True)
    last_name = models.CharField(max_length=32, blank=True, null=True)
    username = models.CharField(max_length=128, blank=True, editable=False)
    email = models.EmailField(max_length=128, blank=True, null=True, unique=True)

    USERNAME_FIELD = 'email'
