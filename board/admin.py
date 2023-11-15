from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')

class PostAdmin():

    list_display = ('title', 'slug', 'status', 'created_on', 'status')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):

    list_display = ('name', 'body', 'post', 'created_on')
    list_filter = ('created_on')
    search_fields = ['name', 'email', 'body']
