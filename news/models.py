from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.utils.html import escape


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
    md5 = models.CharField(max_length=32, unique=True, null=True)
    content = models.URLField(max_length=200)
    published_at = models.DateTimeField()

    def __str__(self):
        return str(self.title)

    def clean(self):
        # escape fields before save
        for field_name in ['title', 'author', 'description', 'content']:
            field_value = getattr(self, field_name)
            setattr(self, field_name, escape(field_value))
        # validate url field
        url_validator = URLValidator()
        try:
            url_validator(self.url)
        except ValidationError as err:
            raise ValidationError({'url validation error': err.message})

        super().clean()