# Generated by Django 5.1.1 on 2024-12-03 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0014_alter_timejogador_jogador_alter_timejogador_time"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="timejogador",
            name="data_termino",
        ),
    ]