# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='cultivo',
            fields=[
                ('idCultivo', models.IntegerField(serialize=False, primary_key=True)),
                ('numeroDeLotes', models.IntegerField()),
                ('jefe', models.CharField(max_length=20)),
                ('dimensiones', models.IntegerField(verbose_name=b'dimensiones en metros cuadrados')),
                ('nombre', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='lote',
            fields=[
                ('idLote', models.IntegerField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=10)),
                ('dimensiones', models.IntegerField(verbose_name=b'dimensiones en metros cuadrados')),
                ('numeroDeEstacas', models.IntegerField()),
                ('idCultivoPertenece', models.IntegerField(verbose_name=b'Cultivo al que pertenece')),
                ('idTrabajadoresAsignados', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='perfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipoUsuario', models.CharField(max_length=10, choices=[(b'D', b'Due\xc3\xb1o'), (b'J', b'Jefe'), (b'T', b'Trabajador')])),
                ('genero', models.CharField(max_length=10, choices=[(b'M', b'Masculino'), (b'F', b'Femenino')])),
                ('tipoDocumento', models.CharField(max_length=20, choices=[(b'C.C', b'Cedula de ciudadania'), (b'T.I', b'Tarjeta de identidad')])),
                ('documento', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.BigIntegerField()),
                ('fechaDeNacimiento', models.DateField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
