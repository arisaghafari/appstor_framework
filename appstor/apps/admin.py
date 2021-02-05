from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title',)
    prepopulated_fields = {'slug' : ('title',)}

admin.site.register(Category, CategoryAdmin)

class AppAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug','status','created', 'updated', 'category_to_str')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug' : ('title',)}
    ordering = ['created', 'updated']
    
    def category_to_str(self, obj):
        return ", ".join([category.title for category in obj.category.all()])


admin.site.register(App, AppAdmin)
admin.site.register(AppSpec)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user' , 'content')
    #search_fields = ('title',)
    #prepopulated_fields = {'slug' : ('title',)}

admin.site.register(Comment, CommentAdmin)