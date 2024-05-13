from django.contrib import admin

# Register your models here.
from .models import Genres, Books, Comment, Like, Dislike


class GenresAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    list_display_links = ('pk', 'name')
    list_filter = ['name']

class BooksAdmin(admin.ModelAdmin):
    list_display = ('pk', 'book', 'created_at', 'genres', 'author')
    list_display_links = ('pk', 'book')
    list_editable = ('genres', 'author')
    list_filter = ('genres', 'book', 'author', 'created_at')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'book', 'created_at', 'author')
    list_display_links = ('pk', 'book')
    list_filter = ('book', 'author', 'created_at')


admin.site.register(Genres, GenresAdmin)
admin.site.register(Books, BooksAdmin)
admin.site.register(Comment, CommentAdmin)
# admin.site.register(Like)
# admin.site.register(Dislike)
