# Generated by Django 5.0.2 on 2024-03-06 15:35

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0005_rename_stage_exam_stage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='Stage',
        ),
        migrations.AddField(
            model_name='exam',
            name='stage',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='exam.stage', verbose_name='Etapa'),
            preserve_default=False,
        ),
    ]