# Generated by Django 5.0.2 on 2024-02-08 19:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('description', models.CharField(max_length=200, verbose_name='Descripción')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_question', models.CharField(max_length=200, null=True, verbose_name='Texto de la Pregunta')),
                ('text_image', models.ImageField(null=True, upload_to='questions', verbose_name='Imagen de la Pregunta')),
                ('answer1', models.CharField(max_length=200, verbose_name='Respuesta A')),
                ('answer2', models.CharField(max_length=200, verbose_name='Respuesta B')),
                ('answer3', models.CharField(max_length=200, null=True, verbose_name='Respuesta C')),
                ('answer4', models.CharField(max_length=200, null=True, verbose_name='Respuesta D')),
                ('correct', models.CharField(max_length=5, verbose_name='Respuesta Correcta')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.module')),
            ],
        ),
    ]