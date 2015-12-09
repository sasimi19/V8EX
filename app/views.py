from django.shortcuts import render
from app.models import BBS, BBS_user, Category, Comment

def index(request):
    articles = BBS.objects.all()
    return render(request, 'index.html', {'articles': articles})

def detail(request, bbs_id):
    article = BBS.objects.get(id=bbs_id)
    comments = Comment.objects.all().filter(article_id=bbs_id)

    # comment_user = Comment.objects.get()
    return render(request, 'detail.html', {'article': article, 'comments': comments})
