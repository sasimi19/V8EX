from django.shortcuts import render
from app.models import BBS, BBS_user, Category, Comment
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.core.validators import RegexValidator
from app.models import BBS_user
from django.template.context_processors import csrf
# from django.contrib.auth import login, authenticate, logout
from django.contrib import auth
import datetime

alphanumeric = RegexValidator(r'^[0-9a-zA-Z\_]*$', '请输入字母、数字、或者下划线')


def index(request):
    articles = BBS.objects.all()
    categories = Category.objects.all()
    comments = Comment.objects.all()
    now = datetime.datetime.now()
    user_count = BBS_user.objects.count()  # 用户数量
    bbs_count = BBS.objects.count() # 帖子数量
    comment_count = Comment.objects.count() # 评论数量
    # categorie = Category.objects.get()aa
    return render(request, 'index.html', {
        'articles': articles,
        'categories': categories,
        'comments': comments,
        'now': now,
        'user_count': user_count,
        'bbs_count': bbs_count,
        'comment_count': comment_count
    })

def detail(request, bbs_id):
    article = BBS.objects.get(id=bbs_id)
    comments = Comment.objects.all().filter(article_id=bbs_id)

    # comment_user = Comment.objects.get()
    return render(request, 'detail.html', {'article': article, 'comments': comments})


def reg(request):
    # if request.method == 'GET':
    #     return render(request, 'reg.html', context_instance=RequestContext(request))

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']
        try:
            alphanumeric(username)
        except:
            messages.add_message(request, messages.WARNING, '用户名只能含有字母、数字或下划线')
            return HttpResponseRedirect(reverse('reg'))

        if BBS_user.objects.filter(user=username).exists():
            messages.add_message(request, messages.WARNING, '用户已存在')
            return HttpResponseRedirect(reverse('reg'))

        if password != password2:
            messages.add_message(request, messages.WARNING, '两次输入的密码不一致，请重新输入')
            return HttpResponseRedirect(reverse('reg'))

        if password == '' or password2 == '':
            messages.add_message(request, messages.WARNING, '密码不能为空')
            return HttpResponseRedirect(reverse('reg'))

        user = BBS_user.objects.create(username=username, email=email, password=password)
        # user = authenticate(username=username, password=password)
        login(request, user)
        p = BBS_user()
        p.user = user
        p.save()
    # return render(request, 'index.html')
        return HttpResponseRedirect(reverse('index'))

def login(request):
    # if request.method == 'GET':
    #     return render(request, 'login.html', context_instance=RequestContext(request))
    #
    # if request.method == 'POST':
    #     try:
    #         user = BBS_user.objects.get(username=request.POST['username'])
    #         if user.password == request.POST['password']:
    #             request.session['user_id'] = user.id
    #             return render(request, 'index.html', {
    #                 'user_logging': user.id,
    #                 'user': user
    #             })
    #
    #         else:
    #             #比较失败，还在login
    #             messages.add_message(request, messages.WARNING, '账号或密码错误，请重新输入')
    #             return HttpResponseRedirect('/login/')
    #     except:
    #          messages.add_message(request, messages.WARNING, '该用户不存在，请重新输入')
    #          return HttpResponseRedirect('/login/')
    # return render(request, 'login.html')
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    print(username, password)
    if user is not None: # and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/')
    else:
        return render(request, 'login.html', {'login_err': 'Wrong username or password!'})




