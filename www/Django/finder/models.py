
from django.db import models
from django.utils import timezone
from datetime import date as d, datetime as dt 

class User(models.Model):
    username = models.CharField(max_length=32) #32 caractères
    password = models.CharField(max_length=64) #taille du hash265
    mail = models.CharField(max_length=320) #taille maximum d'un mail
    website = models.CharField(max_length=255, null=True, blank=True)
    xp = models.PositiveBigIntegerField(default=20)
    level = models.PositiveIntegerField(default=1)
    desc_text = models.TextField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    account_creation = models.DateField(default=d.today())
    permission_level = models.PositiveSmallIntegerField()
    picture_profile = models.ImageField(upload_to='finder/static/finder/img/user/profile_pic',null=True, blank=True)
    picture_profile = models.ImageField(upload_to='finder/static/finder/img/user/banner_pic',null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.username} ({self.mail}) [{self.level}]'

class Licence(models.Model):
    name = models.CharField(max_length=64)
    picture = models.ImageField(upload_to='finder/static/finder/img/licence/',null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    def dataLine(self) -> str:
        return f"{self.name}"

class Tag(models.Model):
    libelle = models.CharField(max_length=64)
    picture = models.ImageField(upload_to='finder/static/finder/img/tag/',null=True, blank=True)

    def __str__(self) -> str:
        return self.libelle

    def dataLine(self) -> str:
        return f"{self.name}"
    

class Platform(models.Model):
    name = models.CharField(max_length=64)
    picture = models.ImageField(upload_to='finder/static/finder/img/platform/',null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
    def dataLine(self) -> str:
        return f"{self.name} {self.description} {self.release_date}"

class Editor(models.Model):
    name = models.CharField(max_length=64)
    release_date = models.DateField(null=True, blank=True)
    still_active = models.BooleanField(default=True)    

    def __str__(self) -> str:
        return self.name
    
    def dataLine(self) -> str:
        return f"{self.name} {self.release_date}"

class Developer(models.Model):
    name = models.CharField(max_length=64)
    release_date = models.DateField(null=True, blank=True)
    isActive = models.BooleanField(default=True)
    isIndependant = models.BooleanField(default=False)

    def dataLine(self) -> str:
        base = ""
        if self.isActive:
            base += "active "
        if self.isIndependant:
            base += "independant"
        return f"{base} {self.name} {self.release_date}"

    def __str__(self) -> str:
        return self.name

class Game(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    release_date = models.DateField(null=True, blank=True)
    isCoop = models.BooleanField(null=True, blank=True)
    isFinished = models.BooleanField(null=True, blank=True)
    isOnline = models.BooleanField(null=True, blank=True)
    isFree = models.BooleanField(null=True, blank=True)
    url = models.CharField(max_length=255 , null=True, blank=True)
    picture = models.ImageField(upload_to='finder/static/finder/img/game/',null=True, blank=True)
    developer = models.ManyToManyField(Developer, blank=True, null=True)
    editor = models.ManyToManyField(Editor, blank=True, null=True)
    platform = models.ManyToManyField(Platform, blank=True, null=True)
    tag = models.ManyToManyField(Tag, blank=True, null=True)
    licence = models.ManyToManyField(Licence, blank=True, null=True)

    def __str__(self) -> str:
        return f"[{self.release_date}] {self.name}" 
    
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
        return f"{base} {self.name} {self.description} {self.release_date} {self.release_date}"

class Submission(models.Model):
    date_creation = models.DateField(default=d.today())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    validated = models.BooleanField(default=False)

    def __str__(self) -> str:
        if self.validated:
            return f"[Verified] {self.user} {self.game} {self.date_creation}"
        else:
            return f"[Unverified] {self.user} {self.game} {self.date_creation}"
        