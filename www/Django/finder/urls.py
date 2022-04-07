from django.urls import path
from . import views

app_name = "finder"

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('games/', views.gameList, name='listGames'),
    path('editors/', views.editorList, name='listEditors'),
    path('devs/', views.devList, name='listDevs'),
    path('tags/', views.tagList, name='listTags'),
    path('platforms/', views.platformList, name='listPlatforms'),
    path('licences/', views.licenceList, name='listLicences'),
    path('game/<int:game_id>/', views.gameDetail, name='detailGame'),
    path('editor/<int:editor_id>/', views.editorDetail, name='detailEditor'),
    path('dev/<int:developer_id>/', views.devDetail, name='detailDev'),
    path('tag/<int:tag_id>/', views.tagDetail, name='detailTag'),
    path('platform/<int:platform_id>/', views.platformDetail, name='detailPlatform'),
    path('licence/<int:licence_id>/', views.licenceDetail, name='detailLicence'),
    path('random/', views.randomPage, name='randomPage'),
    path('search/', views.research, name='search'),
    path('roll/', views.roll, name='roll'),
]
