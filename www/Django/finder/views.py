from tkinter.messagebox import QUESTION
from django.http import HttpResponse
from .models import *
from django.template import loader


def index(request):
    last_submission_list = Submission.objects.filter().order_by('-date_creation')
    template = loader.get_template('finder/index.html')
    data = {'last_submission_list': last_submission_list}
    return HttpResponse(template.render(data, request))

def run(request):
    return HttpResponse("C LA PAGE RUN LOL")

def gameList(request):
    return HttpResponse("C LA GAMELIST LOL")

def pendingSubmissions(request):
    return HttpResponse("Page de liste de submission")