# Generated by Django 4.2.2 on 2023-07-30 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_article_reviews_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='fake_reviews_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]