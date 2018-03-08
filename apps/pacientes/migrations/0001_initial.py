# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import pacientes.models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('establecimientos', '0001_initial'),
        ('cie', '0001_initial'),
        ('ubigeo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AntecedenteFamiliar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('observacion', models.TextField(null=True, verbose_name='Observacion', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('cie', models.ForeignKey(to='cie.ICD10')),
            ],
            options={
                'ordering': ('cie__nombre_mostrar', 'cie__nombre'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AntecedenteGinecologico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tiene_papanicolaou', models.NullBooleanField(default=None, verbose_name='Tiene Papanicolaou')),
                ('fecha_ultimo_papanicolaou', models.DateField(null=True, blank=True)),
                ('resultado_papanicolaou', models.CharField(default=b'no aplica', max_length=20, verbose_name='Resultado Papanicolaou', choices=[(b'no aplica', 'N/A'), (b'normal', 'Normal'), (b'anormal', 'Anormal')])),
                ('lugar_papanicolaou', models.CharField(max_length=100, null=True, verbose_name='Lugar Papanicolaou', blank=True)),
                ('pap_observacion', models.CharField(max_length=255, null=True, verbose_name='Observaci\xf3n', blank=True)),
                ('condon', models.BooleanField(default=False, verbose_name='Condon')),
                ('ovulos', models.BooleanField(default=False, verbose_name='Ovulos')),
                ('diu', models.BooleanField(default=False, verbose_name='DIU')),
                ('inyectable', models.BooleanField(default=False, verbose_name='Inyectable 1 mes')),
                ('inyectable_2', models.BooleanField(default=False, verbose_name='Inyectable 3 meses')),
                ('pastilla', models.BooleanField(default=False, verbose_name='Pastilla')),
                ('implanon', models.BooleanField(default=False, verbose_name='Implanon')),
                ('natural', models.BooleanField(default=False, verbose_name='Natural')),
                ('embarazo_mac', models.NullBooleanField(default=None, verbose_name='Embarazo usando MAC')),
                ('edad_menarquia', models.SmallIntegerField(default=0, null=True, verbose_name='Menarquia edad', blank=True, validators=[django.core.validators.MinValueValidator(8), django.core.validators.MaxValueValidator(20)])),
                ('andria', models.SmallIntegerField(default=0, null=True, verbose_name='Andria', blank=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99)])),
                ('edad_primera_relacion_sexual', models.SmallIntegerField(null=True, verbose_name='Edad primera relacion sexual', blank=True)),
                ('regimen_regular', models.BooleanField(default=True, verbose_name='Regimen Regular')),
                ('duracion_menstruacion', models.SmallIntegerField(default=0, null=True, verbose_name='Duraci\xf3n del ciclo menstrual', blank=True)),
                ('ciclo_menstruacion', models.SmallIntegerField(default=0, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Antecedente Ginecol\xf3gico',
                'verbose_name_plural': 'Antecedente Ginecol\xf3gicos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AntecedenteMedico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('observacion', models.TextField(null=True, verbose_name='Observacion', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('cie', models.ForeignKey(to='cie.ICD10Medical')),
            ],
            options={
                'ordering': ('cie__nombre_mostrar', 'cie__nombre'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AntecedenteObstetrico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gestaciones', models.PositiveSmallIntegerField(default=0)),
                ('abortos', models.PositiveSmallIntegerField(default=0)),
                ('partos', models.PositiveSmallIntegerField(default=0)),
                ('cesareas', models.PositiveSmallIntegerField(default=0, null=True, verbose_name='Ces\xe1reas', blank=True)),
                ('vaginales', models.PositiveSmallIntegerField(default=0, null=True, verbose_name='Vaginales', blank=True)),
                ('rn_mayor_peso', models.SmallIntegerField(default=0, null=True, blank=True)),
                ('nacidos_vivos', models.SmallIntegerField(default=0)),
                ('nacidos_muertos', models.SmallIntegerField(default=0)),
                ('viven', models.SmallIntegerField(default=0)),
                ('muertos_menor_una_sem', models.SmallIntegerField(default=0)),
                ('muertos_mayor_igual_1sem', models.SmallIntegerField(default=0)),
                ('obitos', models.SmallIntegerField(default=0, null=True, blank=True)),
                ('primigesta', models.BooleanField(default=False)),
                ('nacidos_menor_2500g', models.SmallIntegerField(default=0, null=True, blank=True)),
                ('nacidos_menor_37sem', models.SmallIntegerField(default=0, null=True, blank=True)),
                ('preeclampsias', models.SmallIntegerField(default=0, null=True, blank=True)),
                ('hemorragias_postparto', models.SmallIntegerField(default=0, null=True, blank=True)),
                ('embarazos_multiples', models.SmallIntegerField(default=0, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Estudio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('activo', models.BooleanField(default=True, verbose_name='Activo')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Estudio',
                'verbose_name_plural': 'Estudios',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Etnia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('codigo', models.CharField(max_length=10, verbose_name='C\xf3digo')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Etnia',
                'verbose_name_plural': 'Etnias',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoriaClinica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.BigIntegerField(validators=[pacientes.models.validate_hc_length])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('establecimiento', models.ForeignKey(related_name='historias_clinicas', to='establecimientos.Establecimiento')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ocupacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('activo', models.BooleanField(default=True, verbose_name='Activo')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Ocupaci\xf3n',
                'verbose_name_plural': 'Ocupaciones',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('foto', models.ImageField(upload_to=b'fotos', null=True, verbose_name='Foto', blank=True)),
                ('nombres', models.CharField(max_length=100, verbose_name='Nombres')),
                ('apellido_paterno', models.CharField(max_length=50, verbose_name='Apellido Paterno')),
                ('apellido_materno', models.CharField(max_length=50, verbose_name='Apellido Materno')),
                ('tipo_documento', models.CharField(default=b'dni', max_length=10, verbose_name='Tipo Documento', choices=[(b'dni', 'DNI'), (b'pasaporte', 'Pasaporte'), (b'ce', 'CE')])),
                ('numero_documento', models.CharField(max_length=12)),
                ('dni_responsable', models.IntegerField(null=True, verbose_name='DNI del responsable', blank=True)),
                ('nombre_responsable', models.CharField(max_length=70, null=True, verbose_name='Nombre del responsable', blank=True)),
                ('responsable_otros', models.CharField(max_length=100, null=True, verbose_name='Otros', blank=True)),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('transfusion_sanguinea', models.NullBooleanField(default=None, verbose_name='Tranfusion sanguinea')),
                ('tipo_parentesco_responsable', models.CharField(default=b'no aplica', max_length=10, verbose_name='Tipo de parentesco', choices=[(b'no aplica', 'No aplica'), (b'padre', 'Padre'), (b'madre', 'Madre'), (b'pareja', 'Pareja'), (b'otro', 'Otro')])),
                ('direccion', models.CharField(max_length=100, verbose_name='Direcci\xf3n')),
                ('urbanizacion', models.CharField(max_length=100, verbose_name='Sector')),
                ('direccion_completa', models.CharField(max_length=255)),
                ('telefono', models.IntegerField(null=True, verbose_name='Tel\xe9fono de casa', blank=True)),
                ('celular', models.IntegerField(null=True, verbose_name='Celular', blank=True)),
                ('email', models.EmailField(max_length=70, null=True, verbose_name='Correo electronico', blank=True)),
                ('estudio_nombre', models.CharField(default=b'', max_length=100, blank=True)),
                ('tiempo_estudio', models.SmallIntegerField(blank=True, null=True, verbose_name='A\xf1os aprobados', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)])),
                ('ocupacion_nombre', models.CharField(default=b'', max_length=20, blank=True)),
                ('estado_civil', models.CharField(blank=True, max_length=20, null=True, verbose_name='Estado Civil', choices=[(b'soltera', 'Soltera'), (b'conviviente', 'Conviviente'), (b'casada', 'Casada'), (b'divorciada', 'Divorciada'), (b'viuda', 'Viuda')])),
                ('etnia_nombre', models.CharField(default=b'', max_length=20, blank=True)),
                ('seguro_sis', models.BooleanField(default=False, verbose_name='SIS')),
                ('seguro_essalud', models.BooleanField(default=False, verbose_name='Essalud')),
                ('seguro_privado', models.BooleanField(default=False, verbose_name='Privado')),
                ('seguro_sanidad', models.BooleanField(default=False, verbose_name='Sanidad')),
                ('seguro_otros', models.BooleanField(default=False, verbose_name='Otros')),
                ('codigo_afiliacion', models.CharField(max_length=10, verbose_name='C\xf3digo afilicaci\xf3n', blank=True)),
                ('componente', models.CharField(default=b'no aplica', max_length=20, verbose_name='Componente', choices=[(b'no aplica', 'No Aplica'), (b'subsidiado', 'Subsidiado'), (b'semi subsidiado', 'Semi Subsidiado')])),
                ('afiliacion', models.CharField(default=b'no aplica', max_length=20, verbose_name='Afiliacion', choices=[(b'no aplica', 'No Aplica'), (b'nuevo', 'Nuevo'), (b'inscrito', 'Inscrito'), (b'afiliado', 'Afiliado')])),
                ('antecedentes_familiares_niega', models.BooleanField(default=True)),
                ('antecedentes_medicos_niega', models.BooleanField(default=True)),
                ('recibir_sms', models.NullBooleanField(default=None, verbose_name='Recibir SMS')),
                ('celular_wawared', models.IntegerField(null=True, verbose_name='Celular Wawared', blank=True)),
                ('operador', models.CharField(default=b'movistar', max_length=10, verbose_name='Compa\xf1ia Celular', choices=[(b'movistar', 'Movistar'), (b'claro', 'Claro'), (b'nextel', 'Nextel')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('departamento_nacimiento', models.ForeignKey(related_name='nacimiento_pacientes', blank=True, to='ubigeo.Departamento', null=True)),
                ('departamento_residencia', models.ForeignKey(related_name='residencia_pacientes', to='ubigeo.Departamento')),
                ('distrito_residencia', models.ForeignKey(related_name='residencia_pacientes', to='ubigeo.Distrito')),
                ('estudio', models.ForeignKey(blank=True, to='pacientes.Estudio', null=True)),
                ('etnia', models.ForeignKey(blank=True, to='pacientes.Etnia', null=True)),
                ('ocupacion', models.ForeignKey(blank=True, to='pacientes.Ocupacion', null=True)),
                ('pais_nacimiento', models.ForeignKey(related_name='nacimiento_pacientes', to='ubigeo.Pais')),
                ('pais_residencia', models.ForeignKey(related_name='residencia_pacientes', to='ubigeo.Pais')),
                ('provincia_nacimiento', models.ForeignKey(related_name='nacimiento_pacientes', blank=True, to='ubigeo.Provincia', null=True)),
                ('provincia_residencia', models.ForeignKey(related_name='residencia_pacientes', to='ubigeo.Provincia')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RelacionParentesco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=50)),
                ('solo_femenino', models.BooleanField(default=False, verbose_name='Solo femenino')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vacuna',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rubeola', models.NullBooleanField(verbose_name='Rubeola')),
                ('hepatitis_b', models.NullBooleanField(verbose_name='Hepatitis B')),
                ('papiloma', models.NullBooleanField(verbose_name='Papiloma')),
                ('fiebre_amarilla', models.NullBooleanField(verbose_name='Fiebre amarilla')),
                ('h1n1', models.NullBooleanField(verbose_name='H1N1')),
                ('antitetanica_numero_dosis_previas', models.SmallIntegerField(default=0, verbose_name='Numero dosis previas')),
                ('antitetanica_primera_dosis', models.NullBooleanField(default=None, verbose_name='Antitetanica primera dosis')),
                ('antitetanica_primera_dosis_valor', models.CharField(max_length=10, null=True, verbose_name='Antitetanica primera dosis valor', blank=True)),
                ('antitetanica_segunda_dosis', models.NullBooleanField(default=None, verbose_name='Antitetanica segunda dosis')),
                ('antitetanica_segunda_dosis_valor', models.CharField(max_length=10, null=True, verbose_name='Antitetanica segunda dosis valor', blank=True)),
                ('antitetanica_tercera_dosis', models.NullBooleanField(default=None, verbose_name='Antitetanica segunda dosis')),
                ('antitetanica_tercera_dosis_valor', models.CharField(max_length=10, null=True, verbose_name='Antitetanica tercera dosis valor', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('paciente', models.OneToOneField(related_name='vacuna', to='pacientes.Paciente')),
            ],
            options={
                'verbose_name': 'Vacuna',
                'verbose_name_plural': 'Vacunas',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='paciente',
            unique_together=set([('tipo_documento', 'numero_documento')]),
        ),
        migrations.AddField(
            model_name='historiaclinica',
            name='paciente',
            field=models.ForeignKey(related_name='historias_clinicas', to='pacientes.Paciente'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='historiaclinica',
            unique_together=set([('establecimiento', 'numero'), ('establecimiento', 'numero', 'paciente'), ('establecimiento', 'paciente')]),
        ),
        migrations.AddField(
            model_name='antecedenteobstetrico',
            name='paciente',
            field=models.OneToOneField(related_name='antecedente_obstetrico', to='pacientes.Paciente'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='antecedentemedico',
            name='paciente',
            field=models.ForeignKey(related_name='antecedentes_medicos', to='pacientes.Paciente'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='antecedentemedico',
            unique_together=set([('paciente', 'cie')]),
        ),
        migrations.AddField(
            model_name='antecedenteginecologico',
            name='paciente',
            field=models.OneToOneField(related_name='antecedente_ginecologico', to='pacientes.Paciente'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='antecedentefamiliar',
            name='paciente',
            field=models.ForeignKey(related_name='antecedentes_familiares', to='pacientes.Paciente'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='antecedentefamiliar',
            name='relaciones',
            field=models.ManyToManyField(to='pacientes.RelacionParentesco', blank=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='antecedentefamiliar',
            unique_together=set([('paciente', 'cie')]),
        ),
    ]
