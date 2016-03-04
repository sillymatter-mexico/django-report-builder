# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report_builder', '0006_auto_20160303_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='displayfield',
            name='path',
            field=models.CharField(max_length=2000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='displayfield',
            name='path_verbose',
            field=models.CharField(max_length=2000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='displayfield',
            name='report',
            field=models.ForeignKey(blank=True, to='report_builder.Report', null=True),
        ),
        migrations.AlterField(
            model_name='filterfield',
            name='path',
            field=models.CharField(max_length=2000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='filterfield',
            name='path_verbose',
            field=models.CharField(max_length=2000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='filterfield',
            name='report',
            field=models.ForeignKey(blank=True, to='report_builder.Report', null=True),
        ),
    ]
