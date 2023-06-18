# Generated by Django 4.2.2 on 2023-06-13 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pesquisa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colaborador', models.CharField(blank=True, max_length=60, null=True)),
                ('atitude_positiva', models.CharField(blank=True, choices=[('Melhorável', 'Melhorável'), ('Adequado', 'Adequado'), ('Se Destaca', 'Se Destaca'), ('Exemplar', 'Exemplar')], max_length=60, null=True)),
                ('justificativa01', models.TextField(blank=True, null=True)),
                ('trabalho_em_equipe', models.CharField(blank=True, choices=[('Melhorável', 'Melhorável'), ('Adequado', 'Adequado'), ('Se Destaca', 'Se Destaca'), ('Exemplar', 'Exemplar')], max_length=60, null=True)),
                ('justificativa02', models.TextField(blank=True, null=True)),
                ('atendimento_eficaz_cliente', models.CharField(blank=True, choices=[('Melhorável', 'Melhorável'), ('Adequado', 'Adequado'), ('Se Destaca', 'Se Destaca'), ('Exemplar', 'Exemplar')], max_length=60, null=True)),
                ('justificativa03', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
