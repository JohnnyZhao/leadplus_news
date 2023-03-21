from django.views.generic import ListView
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import NewsItem
from .serializers import NewsItemSerializer


class LatestNews(ListView):
    """render the latest 20 news entries as a html page"""
    model = NewsItem
    template_name = 'news/latest.html'
    context_object_name = 'news_items'
    paginate_by = 20

    def get_queryset(self):
        """Get latest 20 news"""
        return NewsItem.objects.filter(
            published_at__lte=timezone.now()).order_by('-published_at')


class LatestNewsAPI(APIView):
    """render the latest 100 news entries"""

    def get(self, request):
        queryset = NewsItem.objects.order_by('-published_at')[:100]
        serializer = NewsItemSerializer(queryset, many=True)
        return Response(serializer.data)
