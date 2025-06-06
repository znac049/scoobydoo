# Generated by Django 5.2.1 on 2025-05-21 09:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileRestoration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
                ('requested', models.DateField()),
                ('notes', models.TextField()),
                ('completed', models.DateField()),
                ('ticket', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='IPAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.GenericIPAddressField(protocol='IPv4')),
                ('server_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MediaType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='StorageLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=30)),
                ('location', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.RESTRICT, to='Doo.storagelocation')),
                ('media_type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Doo.mediatype')),
            ],
        ),
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movement_date', models.DateField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Doo.storagelocation')),
                ('tapes', models.ManyToManyField(to='Doo.tape')),
            ],
        ),
    ]
