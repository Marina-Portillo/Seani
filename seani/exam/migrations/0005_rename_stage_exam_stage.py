# Generated by Django 5.0.2 on 2024-03-06 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_rename_stage_exam_stage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exam',
            old_name='stage',
            new_name='Stage',
        ),
    ]
