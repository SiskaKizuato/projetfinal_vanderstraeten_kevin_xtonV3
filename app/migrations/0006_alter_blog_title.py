# Generated by Django 4.2.2 on 2023-07-18 13:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_blog_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=70, validators=[django.core.validators.MinLengthValidator(40)]),
        ),
    ]
