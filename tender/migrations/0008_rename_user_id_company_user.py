# Generated by Django 4.1 on 2022-10-13 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0007_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='user_id',
            new_name='user',
        ),
    ]