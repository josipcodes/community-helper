from django.contrib import admin
from .models import Category, Task, Profile, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Task)
class TaskAdmin(SummernoteModelAdmin):
    list_display = ('title', 'owner', 'created_date', 'status')
    search_fields = ['title', 'description']
    list_filter = ('status', 'created_date')
    summernote_fields = ('description',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'message', 'post', 'created_date')
    list_filter = ('author', 'created_date')
    search_fields = ['author', 'message', 'post']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'location', 'city')
    list_filter = ('location', 'city')
    search_fields = ['name', 'surname', 'location', 'city', 'country']

