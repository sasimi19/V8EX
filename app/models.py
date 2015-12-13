from django.db import models
from django.contrib.auth.models import User

class BBS(models.Model):
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=256, blank=True, null=True)
    content = models.TextField()
    author = models.ForeignKey('BBS_user')
    category_id = models.ForeignKey('Category', default=1)
    view_count = models.IntegerField()
    created_date = models.DateTimeField()
    update_date = models.DateTimeField()
    ranking = models.IntegerField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.CharField(max_length=128)
    user_id = models.ForeignKey('BBS_user')
    article_id = models.ForeignKey('BBS')
    date = models.DateTimeField()

    def __str__(self):
        return self.content

class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)
    administrator = models.ForeignKey('BBS_user')

    def __str__(self):
        return self.name

class BBS_user(models.Model):
    username = models.OneToOneField(User)
    email = models.EmailField(default='example@email.com')
    signature = models.CharField(max_length=128, default='这家伙很懒，什么也没留下.')
    photo = models.ImageField(upload_to='upload_imgs/', default='upload_imgs/user-0.jpg')

    def __str__(self):
        return self.username.username

