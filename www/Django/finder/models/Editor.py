import django
from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from datetime import date as d, datetime as dt 
import random
from PIL import Image
from .User import User


class Editor(models.Model):
    name = models.CharField(max_length=64)
    release_date = models.DateField(null=True, blank=True)
    still_active = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='finder/static/finder/img/platform/',null=True, blank=True) 
    validated = models.BooleanField(default=False, null=True)
    submitter = models.ManyToManyField(User, blank=True, null=True)
    submit_date = models.DateField(null=True, blank=True, default=now)  

    def __str__(self) -> str:
        return self.name

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
        return f"{self.name} {self.release_date}"

    def getPictureLink(self) -> str:
        return str(self.picture)[14:]

    def getPreInfos(self):
        if len(self.listeDejeu()) < 1: return ""
        elif len(self.listeDejeu()) < 2: return f"Editor of only {self.listeDejeu()[0].name}."
        else:
            alea = random.randint(1, len(self.listeDejeu())) - 1
            alea2 =  len(self.listeDejeu())-1 - alea
            return f"Editor of games like {self.listeDejeu()[alea].name} or {self.listeDejeu()[alea2].name}"

    def listeDejeu(self):
        return self.game_set.all()
    
    def validate(self):
        self.validated = True
