# Generated by Django 4.2.3 on 2023-07-15 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Menu',
            new_name='MenuItem',
        ),
    ]
