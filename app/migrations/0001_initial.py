# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BBS',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64)),
                ('summary', models.CharField(blank=True, max_length=256, null=True)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=16)),
                ('email', models.EmailField(default='example@email.com', max_length=254)),
                ('signature', models.CharField(default='这家伙很懒，什么也没留下.', max_length=128)),
                ('photo', models.ImageField(default='upload_imgs/user-0.jpg', upload_to='upload_imgs/')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=32)),
                ('administrator', models.ForeignKey(to='app.BBS_user')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
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
            field=models.ForeignKey(default=1, to='app.Category'),
        ),
    ]
