# Generated by Django 4.2.2 on 2023-07-30 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_reviewsvisiteur_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='reviews_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]