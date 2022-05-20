from django.http import Http404, HttpResponse
from ..models import *
from django.template import loader
import random


#constantes globales :
global plat_nin, plat_pc, plat_ps, plat_tel, plat_xbox
plat_pc = [28,27,1]
plat_tel = [10,11]
plat_nin = [2,16,17,18,19,20,21,22,23,24,25,26]
plat_xbox = [12,13,14,15]
plat_ps = [3,4,5,6,7,8,9]