# Generated by Django 3.0.5 on 2020-09-16 15:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_pokemonteam_trainer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemonteam',
            name='trainer',
        ),
        migrations.AddField(
            model_name='pokemonteam',
            name='trainer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
