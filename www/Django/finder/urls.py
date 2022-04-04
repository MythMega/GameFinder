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
    path('platform/', views.platformList, name='listPlatform'),
    path('games/<int:game_id>/', views.gameDetail, name='detailGames'),
    path('editors/<int:editor_id>/', views.editorDetail, name='detailEditors'),
    path('devs/<int:developer_id>/', views.devDetail, name='detailDevs'),
    path('tags/<int:tag_id>/', views.tagDetail, name='detailTags'),
    path('platform/<int:platform_id>/', views.platformDetail, name='detailPlatform'),
]
