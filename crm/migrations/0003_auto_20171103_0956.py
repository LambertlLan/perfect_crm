# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 01:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20171102_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('url_name', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name_plural': '菜单表',
            },
        ),
        migrations.AlterField(
            model_name='customer',
            name='consultant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.UserProfile', verbose_name='经手人'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='memo',
            field=models.TextField(blank=True, null=True, verbose_name='备注'),
        ),
        migrations.AddField(
            model_name='role',
            name='menus',
            field=models.ManyToManyField(blank=True, to='crm.Menu'),
        ),
    ]