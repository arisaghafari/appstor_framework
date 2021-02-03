from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title',)
    prepopulated_fields = {'slug' : ('title',)}

admin.site.register(Category, CategoryAdmin)

class AppAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'priority', 'Rate', 'status', 'created', 'updated', 'category_to_str')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug' : ('title',)}
    ordering = ['priority', 'created', 'updated']
    
    def category_to_str(self, obj):
        return 'categories'


admin.site.register(App, AppAdmin)
