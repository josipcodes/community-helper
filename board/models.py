from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, "Draft") (1, "Published"), (2, "Ongoing"), (3, "Archived"))
# Create your models here.
class Post (models.Model):
    title = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasker")
    content = models.TextField
    status = models.IntegerField(choices=STATUS, default=0)
    featured_image = CloudinaryField('image', default='placeholder')
    helper = models.ForeignKey(User, on_delete=models.CASCADE, related_name="helper")
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['created_on']


    def __str__(self):
        return f"Comment {self.body} by {self.name}"