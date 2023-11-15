from django.contrib import admin
from .models import Category, Task, Profile, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Task)
class TaskAdmin(SummernoteModelAdmin):
    list_display = ('title', 'status', 'created_date', 'status')
    search_fields = ['title', 'content']
    prepopulated_fields = {'id': ('title',)}
    list_filter = ('status', 'created_date')
    summernote_fields = ('content',)


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

