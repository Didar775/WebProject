# Generated by Django 4.2 on 2023-05-03 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surfboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='surfboard',
            name='rating',
            field=models.FloatField(default=0),
        ),
    ]
