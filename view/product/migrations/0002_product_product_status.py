# Generated by Django 5.0.2 on 2024-02-28 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_status',
            field=models.BooleanField(default=True),
        ),
    ]
