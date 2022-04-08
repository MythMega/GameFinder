from re import template
from webbrowser import get
from django.http import Http404, HttpResponse
from django.test import tag
from .models import *
from django.template import loader
import random


def index(request):
    last_submission_list = Submission.objects.filter().order_by('-date_creation')
    template = loader.get_template('finder/index.html')
    data = {'last_submission_list': last_submission_list}
    return HttpResponse(template.render(data, request))

def roll(request):
    tags = Tag.objects.all()
    data = {'tags':tags}
    template = loader.get_template('finder/roll.html')
    return HttpResponse(template.render(data, request))

def reroll(request, filtered):
    data = {'gameList': filtered}
    template = loader.get_template('finder/rollresults.html')
    return HttpResponse(template.render(data, request))

def rollResult(request, game_id):
    if game_id == 0:
        allGameList = Game.objects.all()
        valuePrice = str(request.POST['free'])
        valueOnline = str(request.POST['online'])
        valueCoop = str(request.POST['coop'])
        valueInde = str(request.POST['inde'])
        valueRelease = str(request.POST['release'])
        
        #check Price
        if valuePrice == "freeYes":
            allGameList = allGameList.filter(isFree=True)
        elif valuePrice == "freeNo":
            allGameList = allGameList.filter(isFree=False)
        
        ##check Online
        if valueOnline == "onlineYes":
            allGameList = allGameList.filter(isOnline=True)
        elif valueOnline == "onlineYes":
            allGameList = allGameList.filter(isOnline=False)

        ##check Coop
        if valueCoop == "coopYes":
            allGameList = allGameList.filter(isCoop=True)
        elif valueCoop == "coopNo":
            allGameList = allGameList.filter(isCoop=False)

        #check Inde
        if valueInde == "indeYes":
            allGameList = allGameList.filter(isInde=True)
        elif valueInde == "indeNo":
            allGameList = allGameList.filter(isInde=False)

        #check Release
        start = "1900-01-01"
        end = "2999-12-31"
        if valueRelease == "releaseA":
            start = "1900-01-01"
            end = "1989-12-31"
        elif valueRelease == "releaseB":
            start = "1900-01-01"
            end = "1999-12-31"
        elif valueRelease == "releaseC":
            start = "2000-01-01"
            end = "2009-12-31"
        elif valueRelease == "releaseD":
            start = "2010-01-01"
            end = "2019-12-31"
        elif valueRelease == "releaseE":
            start = "2020-01-01"
            end = "2999-12-31"
        allGameList = allGameList.filter(release_date__range=[start,end])

        allTagWanted = []
        allTagUnwanted = []
        stringTagDebug = ""
        for t in Tag.objects.all():
            if request.POST[f'{t.getStringTagLower()}'] == f"{t.getStringTagLower()}Yes":
                allTagWanted.append(t)
                stringTagDebug += f"{t.getStringTagLower()}Yes--"
            elif request.POST[f'{t.getStringTagLower()}'] == f"{t.getStringTagLower()}No":
                allTagUnwanted.append(t)
                stringTagDebug += f"{t.getStringTagLower()}No--"


        monResultat = []
        maListeDeTagQueJeVeuxOuQueJeVeuxPas = allTagWanted + allTagUnwanted
        for unJeu in allGameList:
            ok = True
            for unTag in maListeDeTagQueJeVeuxOuQueJeVeuxPas:
                try :
                    unJeu.tag.get(libelle=unTag.libelle)
                except Tag.DoesNotExist:
                    if unTag in allTagWanted:
                        ok =False
                else:
                    if unTag in allTagUnwanted:
                        ok= False    
            if ok:
                monResultat.append(unJeu)
            

    else:
        data = {'errorMessage': "An error has occured"}
        template = loader.get_template('finder/error404.html')
        return HttpResponse(template.render(data, request))
    data = {'items': monResultat, 'prix':valuePrice, 'coop':valueCoop, 'inde':valueInde, 'date':valueRelease, 'online':valueOnline, 'debugTag':stringTagDebug}
    template = loader.get_template('finder/rollresult.html')
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

def research(request):
    try:
        userSearch = request.POST['searchInput']
        userSearch = userSearch.upper()
    except :
        template = loader.get_template('finder/index.html')
        data = {}
        return HttpResponse(template.render(data, request))
    else:
        t = Tag.objects.all()
        g = Game.objects.all()
        d = Developer.objects.all()
        e = Editor.objects.all()
        p = Platform.objects.all()
        l = Licence.objects.all()
        tags = [];games = [];devs = [];editors = [];platforms = [];licences = []

        for item in t:
            dataItem = item.dataLine().upper()
            if dataItem.find(userSearch) != -1:
                tags.append(item)
        for item in g:
            dataItem = item.dataLine().upper()
            if dataItem.find(userSearch) != -1:
                games.append(item)
        for item in d:
            dataItem = item.dataLine().upper()
            if dataItem.find(userSearch) != -1:
                devs.append(item)
        for item in e:
            dataItem = item.dataLine().upper()
            if dataItem.find(userSearch) != -1:
                editors.append(item)
        for item in p:
            dataItem = item.dataLine().upper()
            if dataItem.find(userSearch) != -1:
                platforms.append(item)
        for item in l:
            dataItem = item.dataLine().upper()
            if dataItem.find(userSearch) != -1:
                licences.append(item)

        template = loader.get_template('finder/search.html')
        data = {'games':games, 'licences':licences, 'devs':devs, 'editors':editors, 'platforms':platforms, 'tags':tags}
        return HttpResponse(template.render(data, request))

    

def randomPage(request):
    t = Tag.objects.order_by("?").first()
    g = Game.objects.order_by("?").first()
    d = Developer.objects.order_by("?").first()
    e = Editor.objects.order_by("?").first()
    p = Platform.objects.order_by("?").first()
    l = Licence.objects.order_by("?").first()
    listToRandom = [t,g,d,e,p,l]
    item = random.choice(listToRandom)
    switcher = {t:"tag", g:"game", d:"dev", e:"editor", p:"platform", l:"licence"}
    template = loader.get_template(f"finder/{switcher[item]}detail.html")
    data = {'item':item}
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