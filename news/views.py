from django.views.generic import ListView
from django.utils import timezone
from django.http import JsonResponse
from .models import NewsItem

class LatestNews(ListView):
    #render the latest 20 news entries as a html page
    model = NewsItem
    template_name = 'news/latest.html'
    context_object_name = 'news_items'
    paginate_by = 20


    def get_queryset(self):
        return NewsItem.objects.filter(published_at__lte=timezone.now()).order_by('-published_at')

def news_items_api(request):
    #return the latest 100 news entries as JSON
    news_items = NewsItem.objects.order_by("-published_at")[:100]
    data = {"news_items": list(news_items.values())}
    return JsonResponse(data)
