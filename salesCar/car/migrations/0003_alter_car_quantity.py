# Generated by Django 5.1.2 on 2024-11-23 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_car_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]