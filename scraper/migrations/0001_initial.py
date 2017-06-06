# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-28 08:19
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
            name='Coins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('symbol', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Coins',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('_db', models.AutoField(primary_key=True, serialize=False)),
                ('rating', models.IntegerField()),
                ('market_cap', models.FloatField()),
                ('price', models.FloatField()),
                ('supply', models.FloatField()),
                ('volume', models.FloatField()),
                ('h1', models.FloatField()),
                ('h24', models.FloatField()),
                ('d7', models.FloatField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('name_coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraper.Coins')),
            ],
            options={
                'get_latest_by': 'pub_date',
                'ordering': ['-pub_date'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='coins',
            unique_together=set([('name', 'symbol')]),
        ),
    ]
