# Generated by Django 4.2.9 on 2024-01-06 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_rename_number_of_guests_booking_no_of_guests'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='no_of_guests',
            new_name='number_of_guests',
        ),
    ]
