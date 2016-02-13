# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='feedbacks',
        ),
        migrations.AddField(
            model_name='feedback',
            name='company',
            field=models.ForeignKey(default='', to='feedback.Company'),
            preserve_default=False,
        ),
    ]
