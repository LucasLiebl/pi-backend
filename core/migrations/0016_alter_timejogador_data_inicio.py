# Generated by Django 5.1.1 on 2024-12-03 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0015_remove_timejogador_data_termino"),
    ]

    operations = [
        migrations.AlterField(
            model_name="timejogador",
            name="data_inicio",
            field=models.DateField(auto_now_add=True),
        ),
    ]
