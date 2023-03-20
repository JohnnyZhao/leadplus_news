import pytz
import requests
from datetime import datetime
from django.utils import timezone
from django.core.management.base import BaseCommand
from news.models import NewsItem
from news.config import NEWS_API_KEY

class Command(BaseCommand):
    help = "Fetches the most recently-published news items from the News API and stores them in the database."

    def handle(self, *args, **options):
        #q is required to call this api
        url = f"https://newsapi.org/v2/everything?q=tech&apiKey={NEWS_API_KEY}&pageSize=100"
        response = requests.get(url)
        if response.status_code != 200:
            self.stdout.write(self.style.ERROR("request failed, status code:%d, error details:\n %s" % (response.status_code, response.text)))
            return
        news_items = response.json()["articles"]
        for news in news_items:
            title = news["title"]
            description = news["description"]
            author = news["author"]
            url = news["url"]
            content = news["content"]

            #publishAt is a datetime string, eg. "2011-11-04T00:05:23Z"
            #need to remove the ending char 'Z' in order to parse it
            published_at = datetime.fromisoformat(news["publishedAt"][:-1])
            #set the timezone to be UTC
            published_at = pytz.utc.localize(published_at)

            NewsItem.objects.create(title=title,
                                    description=description,
                                    author=author,
                                    url=url,
                                    content=content,
                                    published_at=published_at)
        self.stdout.write(self.style.SUCCESS("%d news items successfully fetched and stored in the database." % len(news_items)))
