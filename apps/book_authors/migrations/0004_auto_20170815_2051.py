# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 03:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0003_author_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='note',
            field=models.TextField(null=True, verbose_name=1000),
        ),
    ]
