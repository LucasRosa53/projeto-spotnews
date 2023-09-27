from django.shortcuts import render
from .models import News
# Create your views here.


def req_news(request):
    news_list = {"news": News.objects.all()}
    return render(request, "home.html", news_list)
