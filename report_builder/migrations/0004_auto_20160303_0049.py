# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report_builder', '0003_auto_20150720_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='displayfield',
            name='aggregate',
            field=models.CharField(blank=True, max_length=15, choices=[(b'Sum', b'Sum'), (b'Count', b'Count'), (b'Avg', b'Avg'), (b'Max', b'Max'), (b'Min', b'Min'), (b'Filter', b'Filter')]),
        ),
    ]
