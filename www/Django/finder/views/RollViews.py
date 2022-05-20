from .dependances import *

def roll(request):
    tags = Tag.objects.all()
    data = {'tags':tags}
    template = loader.get_template('finder/roll.html')
    return HttpResponse(template.render(data, request))

def reroll(request):
    liste = request.POST['liste']

    if not len(liste) < 1:
        listsplit = liste.split(";")
        idGame = random.choice(listsplit)
        listsplit.remove(idGame)
        item = Game.objects.get(pk=int(idGame))
        liste = ""
        for i in listsplit:
            liste += i + ";"
    else:
        liste = " "
        item = None
    data = {'liste':liste[:-1], 'item':item}
    template = loader.get_template('finder/rollresult.html')
    return HttpResponse(template.render(data, request))

def rollResult(request, game_id):
    if game_id == 0:
        allGameList = Game.objects.all()
        valuePrice = str(request.POST['free'])
        valueOnline = str(request.POST['online'])
        valueCoop = str(request.POST['coop'])
        valueInde = str(request.POST['inde'])
        valueRelease = str(request.POST['release'])
        valuePlatform = str(request.POST['platform'])
        valueDifficulty = str(request.POST['difficulty'])
        valueMature = str(request.POST['mature'])
        platformFilterOn = False
        if valuePlatform != "platformNC":
            platformFilterOn = True
            #code to get wantedPlatforms = [list of wanted platorms]
            wantedPlatforms = []
            if valuePlatform == "ps":
                wantedPlatforms = plat_ps
            elif valuePlatform == "pc":
                wantedPlatforms = plat_pc
            elif valuePlatform == "tel":
                wantedPlatforms = plat_tel
            elif valuePlatform == "xbox":
                wantedPlatforms = plat_xbox
            elif valuePlatform == "nintendo":
                wantedPlatforms = plat_nin

        #check Price
        if valuePrice == "freeYes":
            allGameList = allGameList.filter(isFree=True)
        elif valuePrice == "freeNo":
            allGameList = allGameList.filter(isFree=False)

        #check Difficulty
        if valueDifficulty == "difficultyYes":
            allGameList = allGameList.filter(isHard=True)
        elif valueDifficulty == "difficultyNo":
            allGameList = allGameList.filter(isHard=False)
        
        #check isMature
        if valueMature == "matureYes":
            allGameList = allGameList.filter(isMature=True)
        elif valueMature == "matureNo":
            allGameList = allGameList.filter(isMature=False)
        
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

        ##check Coop
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

        newGameList = []
        if platformFilterOn:
            #checkPlatform
            for i in allGameList:
                willbeKeept = True
                gameplats = i.platform.all()
                for p in list(gameplats):
                    if p.id not in wantedPlatforms:
                        willbeKeept = False
                if willbeKeept:
                    newGameList.append(i)
            allGameList = newGameList

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
    if len(monResultat) < 1:
        template = loader.get_template('finder/noluck.html')
        return HttpResponse(template.render({}, request))
    selected = random.choice(monResultat)
    futurResultat = monResultat.remove(selected)
    futurResultatStringIds = ""
    random.shuffle(monResultat)
    for i in monResultat:
        futurResultatStringIds += str(i.id) + ";"
    data = {'item': selected, 'liste' : futurResultatStringIds[:-1]}
    template = loader.get_template('finder/rollresult.html')
    return HttpResponse(template.render(data, request))