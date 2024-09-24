# Generated by Django 5.1.1 on 2024-09-23 22:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TicketsApp', '0002_alter_seat_class_type_alter_seat_seat_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='seat',
        ),
        migrations.AddField(
            model_name='passenger',
            name='seat',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='TicketsApp.seat'),
            preserve_default=False,
        ),
    ]