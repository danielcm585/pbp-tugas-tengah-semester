# Generated by Django 4.1 on 2022-10-28 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waste', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='waste',
            name='price',
        ),
        migrations.AddField(
            model_name='waste',
            name='weight',
            field=models.PositiveIntegerField(default=0),
        ),
    ]