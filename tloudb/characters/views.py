from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Character, Games, Groups

def index(request):
    context = {
        'characters': Character.objects.order_by('name')[:6],
    }
    return render(request, 'index.html', context=context)

class CharactersListView(ListView):
    model = Character
    context_object_name = 'characters'
    template_name = 'characters/characters_list.html'

class CharactersDetailView(DetailView):
    model = Character
    context_object_name = 'character'
    template_name = 'characters/character_detail.html'

class GroupsListView(ListView):
    model = Groups
    context_object_name = 'groups'
    template_name = 'groups/groups_list.html'

class GroupsDetailView(DetailView):
    model = Groups
    context_object_name = 'group'
    template_name = 'groups/group_detail.html'

class GamesListView(ListView):
    model = Games
    context_object_name = 'games'
    template_name = 'games/games_list.html'

class GamesDetailView(DetailView):
    model = Games
    context_object_name = 'game'
    template_name = 'games/game_detail.html'