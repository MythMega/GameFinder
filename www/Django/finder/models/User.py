import django
from django.db import models
from django.utils import timezone
from datetime import date as d, datetime as dt 
import random
from PIL import Image


class User(models.Model):
    username = models.CharField(max_length=32) #32 caractères
    password = models.CharField(max_length=64) #taille du hash265
    mail = models.CharField(max_length=320) #taille maximum d'un mail
    website = models.CharField(max_length=255, null=True, blank=True)
    xp = models.PositiveBigIntegerField(default=20)
    level = models.PositiveIntegerField(default=1)
    desc_text = models.TextField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    account_creation = models.DateField(django.utils.timezone.now)
    permission_level = models.PositiveSmallIntegerField()
    picture_profile = models.ImageField(upload_to='finder/static/finder/img/user/profile_pic',null=True, blank=True)
    picture_banner = models.ImageField(upload_to='finder/static/finder/img/user/banner_pic',null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.username} ({self.mail}) [{self.level}]'