from django.contrib.auth import get_user_model
from django.db import models
from django.urls import  reverse

User = get_user_model()
CATEGORY = [
    ('NEWS', 'News'),
    ('EVENT', 'Event'),
]
# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username

class Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    category=models.CharField(max_length=50,choices=CATEGORY)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering=('-timestamp',)
    def __str__(self):
        return self.title
   




