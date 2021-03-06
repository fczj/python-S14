# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 09:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('capation', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=32, verbose_name='用户名')),
                ('password', models.CharField(help_text='pwd', max_length=60)),
                ('user_type_id', models.IntegerField(choices=[(1, '超级用户'), (2, '普通用户'), (3, '普普通用户')], default=1)),
                ('user_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserGroup')),
            ],
        ),
    ]
