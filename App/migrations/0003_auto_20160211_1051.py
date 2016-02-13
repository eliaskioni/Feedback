# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_auto_20160210_0900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='date_created',
        ),
        migrations.AddField(
            model_name='company',
            name='description',
            field=models.TextField(default='default value'),
            preserve_default=False,
        ),
    ]
