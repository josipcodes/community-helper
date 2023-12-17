from django.contrib import admin
from .models import Category, Task, Profile, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Task)
class TaskAdmin(SummernoteModelAdmin):
    '''
    Register TaskAdmin.
    TaskAdmin class organises display, search, filter and summernote field
    '''
    list_display = ('title', 'owner', 'created_date', 'status')
    search_fields = ['title', 'description']
    list_filter = ('status', 'created_date')
    summernote_fields = ('description',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    '''
    Register CommentAdmin.
    CommentAdmin class organises display, search and filter
    '''
    list_display = ('author', 'message', 'post', 'created_date')
    list_filter = ('author', 'created_date')
    search_fields = ['author', 'message', 'post']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''
    Registerting CategoryAdmin.
    '''
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    '''
    Register ProfileAdmin.
    ProfileAdmin class organises display, search and filter
    '''
    list_display = ('person', 'name', 'surname', 'location', 'city')
    list_filter = ('location', 'city')
    search_fields = ['person', 'name', 'surname', 'location', 'city', 'country']

