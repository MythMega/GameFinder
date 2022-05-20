from .dependances import *

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