# Generated by Django 4.1 on 2022-11-01 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marine', '0004_alter_items_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='photo_url',
            field=models.TextField(null=True),
        ),
    ]
