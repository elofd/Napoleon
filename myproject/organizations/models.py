from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    organizations = models.ManyToManyField('Organization')

    USERNAME_FIELD = 'email'


class Organization(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
