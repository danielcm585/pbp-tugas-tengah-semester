# Generated by Django 4.1 on 2022-10-13 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0010_alter_project_closed_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='photo',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
