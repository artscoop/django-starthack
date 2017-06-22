# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 20:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(verbose_name='UUID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='name')),
            ],
            options={
                'verbose_name': 'manufacturer',
                'verbose_name_plural': 'manufacturers',
            },
        ),
        migrations.CreateModel(
            name='TyreModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(verbose_name='UUID')),
                ('name', models.CharField(max_length=64, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('radius', models.FloatField(default=450, help_text='value in mm', verbose_name='radius')),
                ('in_production', models.BooleanField(default=True, verbose_name='in production')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created on')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tyre_models', to='tyres.Manufacturer', verbose_name='manufacturer')),
            ],
            options={
                'verbose_name': 'tyre model',
                'verbose_name_plural': 'tyre models',
            },
        ),
        migrations.AlterUniqueTogether(
            name='tyremodel',
            unique_together=set([('name', 'manufacturer')]),
        ),
    ]
