# Generated by Django 3.2.7 on 2021-10-02 18:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doacao', models.CharField(max_length=255, verbose_name='Doação')),
                ('contato', models.CharField(max_length=255, null=True, verbose_name='Telefone para contato')),
                ('endereco', models.CharField(max_length=255, null=True, verbose_name='Endereço para entrega')),
                ('obs', models.TextField(blank=True, verbose_name='Observação')),
                ('data_1', models.DateTimeField(auto_now_add=True, verbose_name='Data')),
                ('instituicao', models.CharField(choices=[('Instituição_1', 'Instituição_1'), ('Instituição_2', 'Instituição_2')], max_length=150, null=True)),
                ('doador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(max_length=200, verbose_name='Comentar')),
                ('data_2', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('registro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='Registros.registro')),
            ],
        ),
    ]