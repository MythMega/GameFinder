from django.http import Http404, HttpResponse
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

def gameDetail(request, game_id):
    try:
        item = Game.objects.get(pk=game_id)
    except Game.DoesNotExist:
        raise Http404("This game does not exist")
    return Game(request, 'finder/gamedetail.html', {'item':item})



def editorList(request):
    template = loader.get_template('finder/editorlist.html')
    data = {}
    return HttpResponse(template.render(data, request))

def editorDetail(request, editor_id):
    try:
        item = Editor.objects.get(pk=editor_id)
    except Editor.DoesNotExist:
        raise Http404("This editor does not exist")
    return Editor(request, 'finder/editordetail.html', {'item':item})




def devList(request):
    template = loader.get_template('finder/devlist.html')
    data = {}
    return HttpResponse(template.render(data, request))

def devDetail(request, dev_id):
    try:
        item = Developer.objects.get(pk=dev_id)
    except Developer.DoesNotExist:
        raise Http404("This developer does not exist")
    return Developer(request, 'finder/devdetail.html', {'item':item})



def tagList(request):
    template = loader.get_template('finder/taglist.html')
    items = Tag.objects.all()
    data = {'items':items}
    return HttpResponse(template.render(data, request))

def tagDetail(request, tag_id):
    try:
        item = Tag.objects.get(pk=tag_id)
    except Tag.DoesNotExist:
        raise Http404("This tag does not exist")
    return Tag(request, 'finder/tagdetail.html', {'item':item})



def platformList(request):
    template = loader.get_template('finder/platformlist.html')
    data = {}
    return HttpResponse(template.render(data, request))

def platformDetail(request, platform_id):
    try:
        item = Platform.objects.get(pk=platform_id)
    except Platform.DoesNotExist:
        raise Http404("This platform does not exist")
    return Platform(request, 'finder/platformdetail.html', {'item':item})



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