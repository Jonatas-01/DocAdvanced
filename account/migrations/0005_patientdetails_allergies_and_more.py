# Generated by Django 4.2.20 on 2025-03-26 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_doctordetails_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientdetails',
            name='allergies',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patientdetails',
            name='medical_history',
            field=models.TextField(blank=True, null=True),
        ),
    ]
