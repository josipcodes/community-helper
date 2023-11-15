from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django_countries.fields import CountryField


STATUS = (
    ("Draft", "Draft"),
    ("Published", "Published"),
    ("Ongoing", "Ongoing"),#
    ("Archived", "Archived"))
CATEGORIES = (
    ("Helping the elderly", "Helping the elderly"),
    ("Helping the youth", "Helping the youth"),
    ("Helping the people with disability", "Helping the people with disability"),
    ("Grocery run", "Grocery run"),
    ("DIY, minor home improvements", "DIY, minor home improvements"),
    ("Urgent", "Urgent"),
    ("Other", "Other"),
    )
# Create your models here.

class Category (models.Model):
    name = models.CharField(choices=CATEGORIES, null=False, blank=False)
    image = models.CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.name


class Task (models.Model):
    title = models.CharField(max_length=50, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasker")
    description = models.TextField
    status = models.CharField(choices=STATUS, default="Draft")
    helper = models.ForeignKey(User, on_delete=models.CASCADE, related_name="helper")
    created_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="sort")

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey()
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['created_on']


    def __str__(self):
        return f'{self.name}: "{self.message}"'


class Profile(models.Model):
    address = CharField(max_length=100)
    location = CharField(max_length=60)
    city = CharField(max_length=50)
    country = CountryField()
    name = CharField(max_length=50)
    surname = CharField(max_length=50)
    person = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' ' + self.surname