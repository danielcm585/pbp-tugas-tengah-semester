# Generated by Django 4.1 on 2022-10-28 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='photo',
            field=models.TextField(),
        ),
    ]