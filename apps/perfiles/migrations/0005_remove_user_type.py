# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0004_auto_20141119_1446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='type',
        ),
    ]
