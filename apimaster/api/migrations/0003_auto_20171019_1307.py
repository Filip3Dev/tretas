# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-19 16:07
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_coinlist_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coinlist',
            name='ammount',
            field=models.IntegerField(verbose_name='Quantidade de Moedas'),
        ),
        migrations.AlterField(
            model_name='coinlist',
            name='coinslocked',
            field=models.IntegerField(verbose_name='Moedas Travadas'),
        ),
        migrations.AlterField(
            model_name='coinlist',
            name='mcap',
            field=models.CharField(max_length=255, verbose_name='Link do Marketcap'),
        ),
        migrations.AlterField(
            model_name='coinlist',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='coinlist',
            name='nick',
            field=models.CharField(max_length=10, verbose_name='Sigla'),
        ),
        migrations.AlterField(
            model_name='coinlist',
            name='nodecount',
            field=models.IntegerField(verbose_name='Quantidade de Nodes'),
        ),
        migrations.AlterField(
            model_name='coinlist',
            name='price',
            field=models.DecimalField(decimal_places=8, default=Decimal('0E-8'), max_digits=24, verbose_name='Valor em Bitcoin'),
        ),
        migrations.AlterField(
            model_name='coinlist',
            name='roi',
            field=models.IntegerField(verbose_name='ROI'),
        ),
        migrations.AlterField(
            model_name='coinlist',
            name='sharetime',
            field=models.TimeField(verbose_name='Tempo entre Shares'),
        ),
        migrations.AlterField(
            model_name='coinlist',
            name='weekcoins',
            field=models.DecimalField(decimal_places=5, max_digits=10, verbose_name='Moedas geradas na semana'),
        ),
        migrations.AlterField(
            model_name='coinlist',
            name='worth',
            field=models.DecimalField(decimal_places=8, default=Decimal('0E-8'), max_digits=24, verbose_name='Valor Total'),
        ),
    ]
