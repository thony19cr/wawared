# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('embarazos', '0008_planparto_e2_fecha_observacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='embarazo',
            name='perdida_interes_placer',
            field=models.CharField(default=None, max_length=5, null=True, blank=True, choices=[(b'0', b'0'), (b'1', b'1'), (b'2', b'2'), (b'3', b'3')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='embarazo',
            name='triste_deprimida_sin_esperanza',
            field=models.CharField(default=None, max_length=5, null=True, blank=True),
            preserve_default=True,
        ),
    ]
