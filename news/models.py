from django.db import models


class NewsItem(models.Model):
    """News items fetched from newsapi.org
    With hash of the original url as unique key
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50, null=True)
    description = models.TextField()
    url = models.URLField(max_length=200)
    # md5 hash of 'url' to prevent duplicates of the same article
    md5 = models.CharField(max_length=16, unique=True, null=True)
    content = models.URLField(max_length=200)
    published_at = models.DateTimeField()

    def __str__(self):
        return str(self.title)
