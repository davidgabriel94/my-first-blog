# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-14 17:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('universidad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.TextField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('codigo_postal', models.CharField(max_length=6)),
                ('email', models.EmailField(max_length=50)),
                ('fecha_naci', models.DateField()),
                ('universidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='universidad.Universidad')),
            ],
        ),
    ]
