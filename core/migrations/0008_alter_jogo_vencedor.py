# Generated by Django 5.1.1 on 2024-11-07 11:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_jogo_vencedor"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jogo",
            name="vencedor",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name="+", to="core.time"
            ),
        ),
    ]
