# Generated by Django 3.2.7 on 2021-10-16 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_profile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientprofile',
            old_name='bilateral_unilateral_headache',
            new_name='bilateral_headache',
        ),
        migrations.RenameField(
            model_name='patientprofile',
            old_name='headache_pains_questionnaire',
            new_name='electric_headache',
        ),
        migrations.AddField(
            model_name='patientprofile',
            name='oppressive_headache',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patientprofile',
            name='unilateral_headache',
            field=models.BooleanField(default=False),
        ),
    ]