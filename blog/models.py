from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)
    date = models.DateField()
    image = models.ImageField(upload_to='blog/images/', blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
