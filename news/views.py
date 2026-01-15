from django.shortcuts import render
from .models import Article
from django.core.paginator import Paginator


# Create your views here.


def article_display(request):
    articles = Article.objects.all().order_by('-created_at')
    paginator = Paginator(articles, 10)  # 10 записей на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'article_display.html', {'page_obj': page_obj})
