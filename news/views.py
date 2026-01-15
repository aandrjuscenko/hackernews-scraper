from django.shortcuts import render
from .models import Article

# Create your views here.

def article_display(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'article_display.html', {'articles': articles})
