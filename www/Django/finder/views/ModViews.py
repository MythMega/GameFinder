from django.http import Http404, HttpResponse
from ..models import *
from django.template import loader
import random

def modIndex(request):
    return HttpResponse(loader.get_template('finder/mods.html').render({}, request))

def validateAll(request):
    counter = 0
    items = Developer.objects.all().filter(validated=False)
    for i in items:
        i.validate()
        i.save()
        counter +=1
    items = Editor.objects.all().filter(validated=False)
    for i in items:
        i.validate()
        i.save()
        counter +=1
    items = Game.objects.all().filter(validated=False)
    for i in items:
        i.validate()
        i.save()
        counter +=1
    items = Licence.objects.all().filter(validated=False)
    for i in items:
        i.validate()
        i.save()
        counter +=1
    items = Platform.objects.all().filter(validated=False)
    for i in items:
        i.validate()
        i.save()
        counter +=1
    items = Tag.objects.all().filter(validated=False)
    for i in items:
        i.validate()
        i.save()
        counter +=1
    change = counter > 1
    data = {'counter':counter, 'change':change}
    template = loader.get_template('finder/adminsuccess.html')
    return HttpResponse(template.render(data, request))