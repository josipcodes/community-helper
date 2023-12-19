from datetime import datetime # unneccessary?
# from cloudinary.models import CloudinaryField # unneccessary?
from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


STATUS = (
    # ("Draft", "Draft"), # unneccessary?
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
    name = models.CharField(choices=CATEGORIES, null=False, blank=False, max_length=100)
    # image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasker")
    description = models.TextField(max_length=2000)
    status = models.CharField(choices=STATUS, default="Draft", max_length=100)
    helper = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="helper")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="sort", null=False)
    final_date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return self.title

    @property
    def task_snippet(self):
        description_length = len(self.description)
        if description_length > 150:
            return self.description[:150] + '(...)'
        else:
            return self.description

    # @property
    # def countdown(self):
    #     today = datetime.now()
    #     days_time_left = self.final_date - today
    #     days_left = str(days_time_left).split(',', 1)[0]
    #     return days_time_left


class Comment(models.Model):
    # post variable line looks almost identical to the 
    # below, however, it was created without using the source:
    # https://djangocentral.com/creating-comments-system-with-django/
    post = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return f'{self.author}: "{self.message}"'


class Profile(models.Model):
    address = models.CharField(max_length=100)
    location = models.CharField(max_length=60)
    city = models.CharField(max_length=50)
    country = CountryField()
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    person = models.OneToOneField(User, on_delete=models.CASCADE, related_name="users")

    def __str__(self):
        return self.name + ' ' + self.surname
