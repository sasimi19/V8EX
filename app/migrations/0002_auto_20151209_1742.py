# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('content', models.CharField(max_length=128)),
                ('date', models.DateTimeField()),
                ('article_id', models.ForeignKey(to='app.BBS')),
            ],
        ),
        migrations.AlterField(
            model_name='bbs_user',
            name='photo',
            field=models.ImageField(upload_to='upload_imgs/', default='upload_imgs/user-0.jpg'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_id',
            field=models.ForeignKey(to='app.BBS_user'),
        ),
    ]
