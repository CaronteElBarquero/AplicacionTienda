# Generated by Django 2.2 on 2021-10-18 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fac', '0012_auto_20211017_2250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facturadet',
            name='registro',
        ),
        migrations.RemoveField(
            model_name='facturaenc',
            name='registro',
        ),
    ]