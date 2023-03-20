from django.http import JsonResponse
from django.shortcuts import render
from .models import NewsItem

def news_items_page(request):
    #render the latest 20 news entries as a html page
    news_items = NewsItem.objects.order_by("-published_at")[:20]
    return render(request, "news/news_page.html",
                  {"news_items": news_items})

def news_items_api(request):
    #return the latest 100 news entries as JSON
    news_items = NewsItem.objects.order_by("-published_at")[:100]
    data = {"news_items": list(news_items.values())}
    return JsonResponse(data)
