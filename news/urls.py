from django.urls import path
from news.views import req_news


urlpatterns = [
    path("", req_news, name="home-page"),
]
