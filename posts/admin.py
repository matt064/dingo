from django.contrib import admin
from posts.models import Author, Post



class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created', 'modified', 'author']
    list_filter = ['author']
    search_fields = ["title"]

admin.site.register(Post, PostAdmin)



class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nick', 'email', 'biogram']

admin.site.register(Author, AuthorAdmin)