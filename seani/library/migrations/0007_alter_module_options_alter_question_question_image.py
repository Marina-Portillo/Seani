# Generated by Django 5.0.2 on 2024-02-22 18:39

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_alter_module_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='module',
            options={'verbose_name': 'módulo', 'verbose_name_plural': 'módulos'},
        ),
        migrations.AlterField(
            model_name='question',
            name='question_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Imagen de la Pregunta'),
        ),
    ]