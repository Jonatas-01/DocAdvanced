# Generated by Django 4.2.20 on 2025-03-22 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_alter_appointment_status'),
        ('consults', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consult',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='consult',
            name='patient',
        ),
        migrations.AddField(
            model_name='consult',
            name='appointment',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='consult', to='appointments.appointment'),
            preserve_default=False,
        ),
    ]
