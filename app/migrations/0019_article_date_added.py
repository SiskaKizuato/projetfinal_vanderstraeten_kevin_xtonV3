# Generated by Django 4.2.2 on 2023-07-27 21:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_remove_article_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='date_added',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
