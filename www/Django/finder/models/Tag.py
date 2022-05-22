import django
from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from datetime import date as d, datetime as dt 
import random
from PIL import Image
from .User import User

class Tag(models.Model):
    libelle = models.CharField(max_length=64)
    picture = models.ImageField(upload_to='finder/static/finder/img/tag/',null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    validated = models.BooleanField(default=False, null=True)
    submitter = models.ManyToManyField(User, blank=True, null=True)
    submit_date = models.DateField(null=True, blank=True, default=now)

    def getStringTagLower(self) -> str:
        return str(self.libelle).lower()

    def name(self) -> str:
        return str(self.libelle).capitalize()

    def __str__(self) -> str:
        return self.libelle

    def dataLine(self) -> str:
        return f"{self.libelle}"

    def getPictureLink(self) -> str:
        return str(self.picture)[14:]

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

    def getPreInfos(self):
        if len(self.listeDejeu()) < 1: return ""
        elif len(self.listeDejeu()) < 2: return f"Contain only {self.listeDejeu()[0].name}."
        else:
            alea = random.randint(1, len(self.listeDejeu())) - 1
            alea2 =  len(self.listeDejeu()) -1 - alea
            return f"Developer of games like {self.listeDejeu()[alea].name} or {self.listeDejeu()[alea2].name}"

    def listeDejeu(self):
        return self.game_set.all()

    
    def validate(self):
        self.validated = True