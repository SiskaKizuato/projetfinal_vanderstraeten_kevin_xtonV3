# Generated by Django 4.2.2 on 2023-07-30 07:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_delete_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewsVisiteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentaire', models.CharField(max_length=400)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('titre', models.CharField(max_length=100)),
                ('adresseMail', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=50)),
                ('produit_selected', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.article')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentaire', models.CharField(max_length=400)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('titre', models.CharField(max_length=100)),
                ('produit_selected', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_produit_selected', to='app.article')),
                ('redacteure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_redacteure', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
