# Generated by Django 5.1.2 on 2024-11-08 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('rool', models.IntegerField(primary_key=True, serialize=False)),
                ('address', models.TextField()),
                ('father_name', models.TextField()),
            ],
        ),
    ]
