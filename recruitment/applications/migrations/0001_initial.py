# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-29 22:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('applicant_name', models.TextField()),
                ('applicant_gender', models.CharField(max_length=6)),
                ('applicant_birthdate', models.DateField()),
                ('applicant_nationality', models.TextField()),
                ('applicant_residency', models.TextField()),
                ('applicant_major', models.TextField()),
                ('applicant_school', models.TextField()),
                ('applicant_graduation_date', models.DateField()),
                ('applicant_email', models.EmailField(max_length=254)),
                ('applicant_photo', models.ImageField(upload_to='')),
                ('applicant_about', models.TextField(max_length=500)),
            ],
        ),
    ]
