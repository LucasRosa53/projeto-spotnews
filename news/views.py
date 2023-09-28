from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Categories
from .forms import CategoryForm
# Create your views here.


def req_news(request):
    news_list = {"news": News.objects.all()}
    return render(request, "home.html", news_list)


def news_details(request, id):
    news = get_object_or_404(News, pk=id)
    return render(request, "news_details.html", {"news": news})


def category_form(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            Categories.objects.create(name=name)
            return redirect('home-page')
    else:
        form = CategoryForm()
    
    return render(request, 'categories_form.html', {'form': form})
