# Generated by Django 4.2.2 on 2023-07-24 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_delete_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='availability',
        ),
    ]
