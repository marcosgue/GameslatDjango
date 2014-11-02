# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('DNI_CUIT', models.CharField(unique=True, max_length=11)),
                ('email', models.EmailField(max_length=75, blank=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('address', models.CharField(max_length=70, blank=True)),
                ('city', models.CharField(max_length=25, blank=True)),
                ('state', models.CharField(max_length=25, blank=True)),
                ('postal_code', models.CharField(max_length=8, blank=True)),
                ('points', models.PositiveIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
