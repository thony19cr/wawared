# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controles', '0010_auto_20141219_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='control',
            name='ic_ecografia_fecha_1',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='control',
            name='ic_ecografia_fecha_2',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='control',
            name='ic_ecografia_fecha_3',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='control',
            name='ic_enfermeria_fecha_1',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='control',
            name='ic_enfermeria_fecha_2',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='control',
            name='ic_enfermeria_fecha_3',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='control',
            name='ic_laboratorio_fecha_1',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='control',
            name='ic_laboratorio_fecha_2',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='control',
            name='ic_laboratorio_fecha_3',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='control',
            name='ic_medicina_fecha_1',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='control',
            name='ic_medicina_fecha_2',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='control',
            name='ic_medicina_fecha_3',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='control',
            name='ic_nutricion_fecha_1',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='control',
            name='ic_nutricion_fecha_2',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='control',
            name='ic_nutricion_fecha_3',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='control',
            name='ic_odontologia_fecha_1',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='control',
            name='ic_odontologia_fecha_2',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='control',
            name='ic_odontologia_fecha_3',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='control',
            name='ic_psicologia_fecha_1',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='control',
            name='ic_psicologia_fecha_2',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='control',
            name='ic_psicologia_fecha_3',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]