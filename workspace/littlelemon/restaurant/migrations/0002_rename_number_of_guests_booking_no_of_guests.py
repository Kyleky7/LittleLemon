# Generated by Django 4.2.9 on 2024-01-06 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='number_of_guests',
            new_name='no_of_guests',
        ),
    ]
