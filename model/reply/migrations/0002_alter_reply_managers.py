# Generated by Django 5.0.2 on 2024-02-21 13:24

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reply', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='reply',
            managers=[
                ('enabled_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
