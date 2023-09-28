from django.shortcuts import render, get_object_or_404
from .models import News
# Create your views here.


def req_news(request):
    news_list = {"news": News.objects.all()}
    return render(request, "home.html", news_list)


def news_details(request, id):
    news = get_object_or_404(News, pk=id)
    return render(request, "news_details.html", {"news": news})
