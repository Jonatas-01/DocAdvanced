# Generated by Django 4.2.20 on 2025-03-18 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_alter_appointment_doctor_alter_appointment_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('rejected', 'Rejected'), ('closed', 'Closed'), ('canceled', 'Canceled')], default='pending', max_length=10),
        ),
    ]
