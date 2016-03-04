# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report_builder', '0004_auto_20160303_0049'),
    ]

    operations = [
        migrations.AddField(
            model_name='displayfield',
            name='exclude',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='displayfield',
            name='filter_type',
            field=models.CharField(default=b'icontains', max_length=20, null=True, blank=True, choices=[(b'exact', b'Equals'), (b'iexact', b'Equals (case-insensitive)'), (b'contains', b'Contains'), (b'icontains', b'Contains (case-insensitive)'), (b'in', b'in (comma seperated 1,2,3)'), (b'gt', b'Greater than'), (b'gte', b'Greater than equals'), (b'lt', b'Less than'), (b'lte', b'Less than equals'), (b'startswith', b'Starts with'), (b'istartswith', b'Starts with (case-insensitive)'), (b'endswith', b'Ends with'), (b'iendswith', b'Ends with  (case-insensitive)'), (b'range', b'range'), (b'week_day', b'Week day'), (b'isnull', b'Is null'), (b'regex', b'Regular Expression'), (b'iregex', b'Reg. Exp. (case-insensitive)'), (b'max', b'Max (annotation-filter)'), (b'min', b'Min (annotation-filter)')]),
        ),
        migrations.AddField(
            model_name='displayfield',
            name='filter_value',
            field=models.CharField(max_length=2000, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='displayfield',
            name='filter_value2',
            field=models.CharField(max_length=2000, null=True, blank=True),
        ),
    ]
