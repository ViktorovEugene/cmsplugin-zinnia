# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-09 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_zinnia', '0003_latestentriesplugin_app'),
    ]

    operations = [
        migrations.AddField(
            model_name='randomentriesplugin',
            name='app',
            field=models.CharField(blank=True, choices=[('', '-------'), ('blog', 'Blog'), ('press', 'Press')], db_index=True, default='', max_length=50, verbose_name='application'),
        ),
    ]
