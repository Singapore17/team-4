# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-29 04:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllocationTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantitiy', models.IntegerField()),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BeneficiariesTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('size', models.IntegerField()),
                ('priority', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DonationsTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_qty', models.IntegerField()),
                ('expiry', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='DonorsTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('contact', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ItemTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StockCountTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DbController.ItemTable')),
            ],
        ),
        migrations.AddField(
            model_name='donationstable',
            name='donor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DbController.DonorsTable'),
        ),
        migrations.AddField(
            model_name='donationstable',
            name='item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DbController.ItemTable'),
        ),
        migrations.AddField(
            model_name='allocationtable',
            name='beneficiaries',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DbController.BeneficiariesTable'),
        ),
        migrations.AddField(
            model_name='allocationtable',
            name='item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DbController.ItemTable'),
        ),
    ]
