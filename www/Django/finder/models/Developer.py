import django
from django.db import models
from django.utils import timezone
from datetime import date as d, datetime as dt 
import random
from PIL import Image


class Developer(models.Model):
    name = models.CharField(max_length=64)
    release_date = models.DateField(null=True, blank=True)
    isActive = models.BooleanField(default=True)
    isIndependant = models.BooleanField(default=False)
    picture = models.ImageField(upload_to='finder/static/finder/img/platform/',null=True, blank=True)
    description = models.TextField(null=True, blank=True)

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

    def dataLine(self) -> str:
        base = ""
        if self.isActive:
            base += "active "
        if self.isIndependant:
            base += "independant"
        return f"{base} {self.name} {self.release_date}"

    def __str__(self) -> str:
        return self.name

    def getPictureLink(self) -> str:
        return str(self.picture)[14:]

    def getPreInfos(self) -> str:
        if len(self.listeDejeu()) < 1: return ""
        elif len(self.listeDejeu()) < 2: return f"Developer of only {self.listeDejeu()[0].name}."
        else:
            alea = random.randint(1, len(self.listeDejeu())) - 1
            alea2 =  len(self.listeDejeu())-1 - alea
            return f"Developer of games like {self.listeDejeu()[alea].name} or {self.listeDejeu()[alea2].name}"

    def listeDejeu(self):
        return self.game_set.all()