import django
from django.db import models
from django.utils import timezone
from datetime import date as d, datetime as dt 
import random
from PIL import Image
from .Developer import *
from .Editor import *
from .Platform import *
from .Tag import *
from .Licence import *
from django.utils.timezone import now
from .User import User



class Game(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    release_date = models.DateField(null=True, blank=True)
    isCoop = models.BooleanField(null=True, blank=True)
    isFinished = models.BooleanField(null=True, blank=True)
    isOnline = models.BooleanField(null=True, blank=True)
    isFree = models.BooleanField(null=True, blank=True)
    isHard = models.BooleanField(null=True, blank=True)
    isMature = models.BooleanField(null=True, blank=True)
    isInde = models.BooleanField(null=True, blank=True)
    url = models.CharField(max_length=255 , null=True, blank=True)
    picture_icon = models.ImageField(upload_to='finder/static/finder/img/game/',null=True, blank=True)
    picture_banner = models.ImageField(upload_to='finder/static/finder/img/game/',null=True, blank=True)
    picture_gameplay = models.ImageField(upload_to='finder/static/finder/img/game/',null=True, blank=True)
    developer = models.ManyToManyField(Developer, blank=True, null=True)
    editor = models.ManyToManyField(Editor, blank=True, null=True)
    platform = models.ManyToManyField(Platform, blank=True, null=True)
    tag = models.ManyToManyField(Tag, blank=True, null=True)
    licence = models.ManyToManyField(Licence, blank=True, null=True)
    validated = models.BooleanField(default=False, null=True)
    submitter = models.ManyToManyField(User, blank=True, null=True)
    submit_date = models.DateField(null=True, blank=True, default=now)

    def getShortDesc(self) -> str:
        stringDesc = str(self.description)
        t = stringDesc.split(" ")
        resultat = ""
        lenght = len(t)
        if lenght>24:
            motAffiche = 24
        else:
            motAffiche = lenght
        for i in range(motAffiche):
            resultat += t[i] + " "
        resultat += "..."
        return resultat

    # def isInde(self) -> bool:
    #     ed = self.editor.all()
    #     if len(ed) == 0:
    #         return True
    #     else:
    #         return False


    def __str__(self) -> str:
        return f"[{self.release_date.year}] {self.name}"

    

    def getPictureLink(self) -> str:
        return str(self.picture_icon)[14:]

    def getBannerLink(self) -> str:
        return str(self.picture_banner)[14:]

    def getGameplayLink(self) -> str:
        return str(self.picture_gameplay)[14:]
    
    def dataLine(self) -> str:
        base = ""
        if self.isOnline:
            base += "Online "
        else:
            base += "Offline "
        if self.isCoop:
            base += "Coop "
        if self.isFree:
            base += "Free "
        else:
            base += "paid "
        return f"{base} {self.name} {self.release_date} {self.release_date}"
