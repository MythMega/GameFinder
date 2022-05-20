from .dependances import *

def index(request):
    #last_submission_list = Submission.objects.filter().order_by('-date_creation')
    last_submission_list = []
    template = loader.get_template('finder/index.html')
    data = {'last_submission_list': last_submission_list}
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