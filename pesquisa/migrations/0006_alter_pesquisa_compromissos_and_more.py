# Generated by Django 4.2.2 on 2023-06-17 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pesquisa', '0005_pesquisa_compromissos_pesquisa_pontos_fortes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesquisa',
            name='compromissos',
            field=models.TextField(blank=True, max_length=60, null=True, verbose_name='Compromissos Estabelecidos:'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='pontos_fortes',
            field=models.TextField(blank=True, max_length=60, null=True, verbose_name='Pontos Fortes:'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='pontos_reforçar',
            field=models.TextField(blank=True, max_length=60, null=True, verbose_name='Pontos a Reforçar:'),
        ),
    ]
