from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('characters-list/', views.CharactersListView.as_view(), name='characters'),
    path('characters-list/<int:pk>', views.CharactersDetailView.as_view(), name='detail'),
    path('groups-list/', views.GroupsListView.as_view(), name='groups'),
    path('groups-list/<int:pk>', views.GroupsDetailView.as_view(), name='group'),
    path('games-list/', views.GamesListView.as_view(), name='games'),
    path('games-list/<int:pk>', views.GamesDetailView.as_view(), name='game')
]