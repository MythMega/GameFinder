from django.contrib import admin
from .models import *


admin.site.register(Game)
admin.site.register(Developer)
admin.site.register(Editor)
admin.site.register(Licence)
admin.site.register(Platform)
admin.site.register(Tag)
admin.site.register(User)