from django.db import models

class NewsItem(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    description = models.TextField()
    url = models.URLField(max_length=200)
    content = models.URLField(max_length=200)
    published_at = models.DateTimeField()

    def __str__(self):
        return self.title
