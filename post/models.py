from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="post/%Y/%m/%d/", null=True, blank=True)
    content = models.TextField()

    def __str__(self):
        return self.title