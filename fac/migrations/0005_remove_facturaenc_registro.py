# Generated by Django 2.2 on 2021-10-18 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fac', '0004_facturaenc_registro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facturaenc',
            name='registro',
        ),
    ]
