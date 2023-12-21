from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


STATUS = (
    # Draft is only available to the staff within the admin panel
    ("Draft", "Draft"),
    ("Published", "Published"),
    ("Ongoing", "Ongoing"),
    ("Archived", "Archived"))

CATEGORIES = (
    ("1", "Helping the elderly"),
    ("2", "Helping the youth"),
    ("3", "Helping the people with disability"),
    ("4", "Grocery run"),
    ("5", "DIY, minor home improvements"),
    ("6", "Urgent"),
    ("7", "Other"),
    )


class Category(models.Model):
    '''
    Category contains a name, with 7 choices.
    '''
    name = models.CharField(
        choices=CATEGORIES, null=False, blank=False, max_length=100
        )

    def __str__(self):
        return self.name


class Task(models.Model):
    '''
    Task model used to create task.
    '''
    title = models.CharField(max_length=50)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="tasker"
        )
    description = models.TextField(max_length=2000)
    status = models.CharField(choices=STATUS, default="Draft", max_length=100)
    helper = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="helper"
        )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="sort", null=False
        )
    final_date = models.DateField(blank=True, null=True)

    class Meta:
        '''
        Ordering from oldest to newest.
        '''
        ordering = ['created_date']

    def __str__(self):
        '''
        Function task returns a task title.
        '''
        return self.title

    @property
    def task_snippet(self):
        '''
        Task snippet displays 150 characters followed by '...',
        if there are sufficient characters.
        '''
        description_length = len(self.description)
        if description_length > 150:
            return self.description[:150] + '(...)'
        else:
            return self.description


class Comment(models.Model):
    '''
    Comment model used to create a comment.
    '''
    # post variable line looks almost identical to the
    # below, however, it was created without using the source:
    # https://djangocentral.com/creating-comments-system-with-django/
    post = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name="comments"
        )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
        )
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        '''
        Ordering from oldest to newest.
        '''
        ordering = ['created_date']

    def __str__(self):
        '''
        Functionn returns author and their comment.
        '''
        return f'{self.author}: "{self.message}"'


class Profile(models.Model):
    '''
    Profile model used to create a profile.
    '''
    address = models.CharField(max_length=100)
    location = models.CharField(max_length=60)
    city = models.CharField(max_length=50)
    country = CountryField()
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    person = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="users"
        )

    def __str__(self):
        '''
        Function returns the first and the last name of a user.
        '''
        return self.name + ' ' + self.surname
