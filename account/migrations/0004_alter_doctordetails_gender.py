# Generated by Django 4.2.20 on 2025-03-13 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_patientdetails_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctordetails',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6),
        ),
    ]
