# Generated by Django 5.1.1 on 2024-12-13 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_alter_time_escudo'),
    ]

    operations = [
        migrations.AddField(
            model_name='jogo',
            name='jogo_realizado',
            field=models.BooleanField(default=False),
        ),
    ]
