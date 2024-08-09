# Generated by Django 5.0.8 on 2024-08-09 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_rename_agent_name_agent_agent_position'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agent',
            old_name='agent_position',
            new_name='agent_job_title',
        ),
        migrations.AddField(
            model_name='agent',
            name='agent_name',
            field=models.TextField(blank=True),
        ),
    ]
