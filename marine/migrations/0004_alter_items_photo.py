# Generated by Django 4.1 on 2022-10-31 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marine', '0003_alter_items_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]