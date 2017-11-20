# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 01:45
from __future__ import unicode_literals

import artdb.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('profile_img', models.ImageField(blank=True, null=True, upload_to=artdb.models.scramble_profile_image)),
                ('bod', models.CharField(blank=True, max_length=8, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to=artdb.models.scramble_uploaded_image)),
                ('size', models.CharField(blank=True, max_length=100, null=True)),
                ('style', models.CharField(blank=True, max_length=100, null=True)),
                ('created', models.CharField(blank=True, max_length=20, null=True)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artworks', to='artdb.Artist')),
            ],
        ),
        migrations.CreateModel(
            name='PriceHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=8)),
                ('begin', models.IntegerField(blank=True, null=True)),
                ('estimate_low', models.IntegerField(blank=True, null=True)),
                ('estimate_high', models.IntegerField(blank=True, null=True)),
                ('hammer', models.IntegerField(blank=True, null=True)),
                ('sold', models.BooleanField()),
                ('artwork', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='price_history', to='artdb.Artwork')),
            ],
        ),
    ]
