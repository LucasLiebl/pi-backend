# Generated by Django 5.1.1 on 2024-10-29 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_alter_time_derrota_alter_time_gols_contra_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="time",
            name="empate",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
