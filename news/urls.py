from django.urls import path
from news.views import req_news, news_details
from .views import category_form


urlpatterns = [
    path("", req_news, name="home-page"),
    path("news/<int:id>", news_details, name="news-details-page"),
    path('categories/', category_form, name='categories-form'),
]
