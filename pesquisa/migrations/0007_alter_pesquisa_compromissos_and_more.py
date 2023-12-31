# Generated by Django 4.2.2 on 2023-06-17 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pesquisa', '0006_alter_pesquisa_compromissos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesquisa',
            name='compromissos',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='justificativa01',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='pontos_fortes',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='pontos_reforçar',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name=''),
        ),
    ]
