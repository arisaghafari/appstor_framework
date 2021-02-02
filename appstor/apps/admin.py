from django.contrib import admin
from .models import App

class AppAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'priority', 'Rate', 'status', 'created', 'updated')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug' : ('title',)}
    ordering = ['priority', 'created', 'updated']

admin.site.register(App, AppAdmin)
