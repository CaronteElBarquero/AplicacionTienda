# Generated by Django 2.2 on 2021-10-18 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fac', '0013_auto_20211017_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='facturadet',
            name='registro',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='facturaenc',
            name='registro',
            field=models.IntegerField(default=0),
        ),
    ]
