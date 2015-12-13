# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BBS',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=64)),
                ('summary', models.CharField(blank=True, null=True, max_length=256)),
                ('content', models.TextField()),
                ('view_count', models.IntegerField()),
                ('created_date', models.DateTimeField()),
                ('update_date', models.DateTimeField()),
                ('ranking', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BBS_user',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('signature', models.CharField(default='这家伙很懒，什么也没留下.', max_length=128)),
                ('photo', models.ImageField(upload_to='upload_imgs/', default='upload_imgs/user-0.jpg')),
                ('username', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=32)),
                ('administrator', models.ForeignKey(to='app.BBS_user')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('content', models.CharField(max_length=128)),
                ('date', models.DateTimeField()),
                ('article_id', models.ForeignKey(to='app.BBS')),
                ('user_id', models.ForeignKey(to='app.BBS_user')),
            ],
        ),
        migrations.AddField(
            model_name='bbs',
            name='author',
            field=models.ForeignKey(to='app.BBS_user'),
        ),
        migrations.AddField(
            model_name='bbs',
            name='category_id',
            field=models.ForeignKey(to='app.Category', default=1),
        ),
    ]
