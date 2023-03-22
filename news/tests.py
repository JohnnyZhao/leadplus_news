import hashlib
import pytz
from datetime import datetime, timezone, timedelta
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import NewsItem
from .serializers import NewsItemSerializer


class NewsItemSignalTestCase(TestCase):
    def test_calculate_md5(self):
        utc_tz = pytz.timezone('UTC')
        news = NewsItem.objects.create(
            title="Test News",
            author="Test Author",
            description="Test Description",
            url="http://www.example.com/test-news",
            content="Test Content",
            published_at=datetime.now(utc_tz),
        )
        self.assertIsNotNone(news.md5)
        md5_hash = hashlib.md5(news.url.encode('utf-8')).hexdigest()
        self.assertEqual(news.md5, md5_hash)


class LatestNewsAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('news-items-api')

        # create some news items for testing
        now = datetime.now(timezone.utc)
        NewsItem.objects.create(title='News 1', url='http://example.com/1', published_at=now - timedelta(days=2))
        NewsItem.objects.create(title='News 2', url='http://example.com/2', published_at=now - timedelta(days=1))
        NewsItem.objects.create(title='News 3', url='http://example.com/3', published_at=now - timedelta(hours=1))

    def test_get_latest_news(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # check that the latest 100 news items are returned, ordered by published_at descending
        expected_queryset = NewsItem.objects.order_by('-published_at')[:100]
        expected_data = NewsItemSerializer(expected_queryset, many=True).data
        self.assertEqual(response.data, expected_data)