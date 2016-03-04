# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report_builder', '0005_auto_20160303_0052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='displayfield',
            name='exclude',
        ),
        migrations.RemoveField(
            model_name='displayfield',
            name='filter_type',
        ),
        migrations.RemoveField(
            model_name='displayfield',
            name='filter_value',
        ),
        migrations.RemoveField(
            model_name='displayfield',
            name='filter_value2',
        ),
        migrations.AddField(
            model_name='displayfield',
            name='filter_field',
            field=models.ForeignKey(blank=True, to='report_builder.FilterField', null=True),
        ),
    ]
