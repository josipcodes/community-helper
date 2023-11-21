from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django_countries.fields import CountryField


STATUS = (
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
# Create your models here.

class Category (models.Model):
    name = models.CharField(choices=CATEGORIES, null=False, blank=False, max_length=100)
    image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.name


class Task (models.Model):
    title = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasker")
    description = models.TextField(max_length=2000)
    status = models.CharField(choices=STATUS, default="Draft", max_length=100)
    helper = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="helper")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="sort", null=False)
    # category = models.ManyToOneRel(Category.name, on_delete=models.CASCADE)
    final_date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return self.title

    @property
    def countdown(self):
        today = date.today()
        days_time_left = self.final_date - today
        days_left = str(days_time_left).split(',', 1)[0]
        return days_left


class Comment(models.Model):
    post = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['created_date']


    def __str__(self):
        return f'{self.author.user.profile.name}: "{self.message}"'


class Profile(models.Model):
    address = models.CharField(max_length=100)
    location = models.CharField(max_length=60)
    city = models.CharField(max_length=50)
    country = CountryField()
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    person = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = CloudinaryField('image', default='placeholder-avatar')

    def __str__(self):
        return self.name + ' ' + self.surname


# class Review(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     karma = models.ManyToManyField(User, related_name='karma_points', blank=True)
#     post = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="task")

#     def karma_points(self):
#         return self.karma.count() / self.karma.len