from tkinter.messagebox import QUESTION
from django.http import HttpResponse
from .models import *
from django.template import loader


def index(request):
    last_submission_list = Submission.objects.filter().order_by('-date_creation')
    template = loader.get_template('finder/index.html')
    data = {'last_submission_list': last_submission_list}
    return HttpResponse(template.render(data, request))

def gameList(request):
    template = loader.get_template('finder/gamelist.html')
    data = {}
    return HttpResponse(template.render(data, request))

def pendingSubmissions(request):
    template = loader.get_template('finder/pendingSubmission.html')
    data = {}
    return HttpResponse(template.render(data, request))

def login(request):
    template = loader.get_template('finder/login.html')
    data = {}
    return HttpResponse(template.render(data, request))

def register(request):
    template = loader.get_template('finder/register.html')
    data = {}
    return HttpResponse(template.render(data, request))

def logout(request):
    template = loader.get_template('finder/logout.html')
    data = {}
    return HttpResponse(template.render(data, request))

def profile(request):
    template = loader.get_template('finder/profile.html')
    data = {}
    return HttpResponse(template.render(data, request))