from .dependances import *


def gameList(request):
    template = loader.get_template('finder/gamelist.html')
    items = Game.objects.all()
    data = {'items': items}
    return HttpResponse(template.render(data, request))

def gameDetail(request, game_id):
    try:
        item = Game.objects.get(pk=game_id)
    except Game.DoesNotExist:
        raise Http404("This game does not exist")
    data = {'item':item, 'pic':item.getPictureLink()}
    template = loader.get_template('finder/gamedetail.html')
    return HttpResponse(template.render(data, request))

def editorList(request):
    template = loader.get_template('finder/editorlist.html')
    items = Editor.objects.all()
    itemList = {}
    for item in items:
        itemList[item] = item.getPictureLink()
    data = {'itemList': itemList}
    return HttpResponse(template.render(data, request))

def editorDetail(request, editor_id):
    try:
        item = Editor.objects.get(pk=editor_id)
    except Editor.DoesNotExist:
        raise Http404("This editor does not exist")
    data = {'item':item, 'pic':item.getPictureLink()}
    template = loader.get_template('finder/editordetail.html')
    return HttpResponse(template.render(data, request))

def licenceList(request):
    template = loader.get_template('finder/licencelist.html')
    items = Licence.objects.all()
    itemList = {}
    for item in items:
        itemList[item] = item.getPictureLink()
    data = {'itemList': itemList}
    return HttpResponse(template.render(data, request))

def licenceDetail(request, licence_id):
    try:
        item = Licence.objects.get(pk=licence_id)
    except Licence.DoesNotExist:
        raise Http404("This licence does not exist")
    data = {'item':item, 'pic':item.getPictureLink()}
    template = loader.get_template('finder/licencedetail.html')
    return HttpResponse(template.render(data, request))

def devList(request):
    template = loader.get_template('finder/devlist.html')
    items = Developer.objects.all()
    itemList = {}
    for item in items:
        itemList[item] = item.getPictureLink()
    data = {'itemList': itemList}
    return HttpResponse(template.render(data, request))

def devDetail(request, developer_id):
    try:
        item = Developer.objects.get(pk=developer_id)
    except Developer.DoesNotExist:
        raise Http404("This licence does not exist")
    data = {'item':item, 'pic':item.getPictureLink()}
    template = loader.get_template('finder/devdetail.html')
    return HttpResponse(template.render(data, request))

def tagList(request):
    template = loader.get_template('finder/taglist.html')
    items = Tag.objects.all()
    itemList = {}
    for item in items:
        itemList[item] = str(item.getPictureLink())
    data = {'itemList': itemList}
    return HttpResponse(template.render(data, request))

def tagDetail(request, tag_id):
    try:
        item = Tag.objects.get(pk=tag_id)
    except Tag.DoesNotExist:
        raise Http404("This tag does not exist")
    data = {'item':item, 'pic':item.getPictureLink()}
    template = loader.get_template('finder/tagdetail.html')
    return HttpResponse(template.render(data, request))

def platformList(request):
    template = loader.get_template('finder/platformlist.html')
    items = Platform.objects.all()
    itemList = {}
    for item in items:
        itemList[item] = str(item.getPictureLink())
    data = {'itemList': itemList}
    return HttpResponse(template.render(data, request))

def platformDetail(request, platform_id):

    try:
        item = Platform.objects.get(pk=platform_id)
    except Platform.DoesNotExist:
        raise Http404("This tag does not exist")
    data = {'item':item, 'pic':item.getPictureLink()}
    template = loader.get_template('finder/platformdetail.html')
    return HttpResponse(template.render(data, request))

def pendingSubmissions(request):
    template = loader.get_template('finder/pendingSubmission.html')
    data = {}
    return HttpResponse(template.render(data, request))

