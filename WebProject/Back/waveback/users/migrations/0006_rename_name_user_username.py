# Generated by Django 4.2 on 2023-05-03 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_user_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='username',
        ),
    ]