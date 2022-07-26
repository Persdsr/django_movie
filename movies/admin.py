from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

class MoviesAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_photo_url')
    list_display_links = ('name', 'get_photo_url')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

    def get_photo_url(self, object):
        if object.poster:
            return mark_safe(f"<img src='{object.poster.url}' width=200px; height=150px;>")

class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_photo_url')
    list_display_links = ('name', 'get_photo_url')

    def get_photo_url(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=200px; height=150px;>")

@admin.register(Contact)
class ContactAmin(admin.ModelAdmin):
    list_display = ('name', 'email')

admin.site.register(Movies, MoviesAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Director)
admin.site.register(Logo)
admin.site.register(Comments)

#@admin.register(Contact)
#class ContactAdmin(admin.ModelAdmin):
#    list_display = ('name', 'email')

#test git