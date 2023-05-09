from django.contrib import admin

from .models import Character, Groups, Games

# Register your models here.

admin.site.register(Character)
admin.site.register(Groups)
admin.site.register(Games)