# Generated by Django 3.2.4 on 2021-08-30 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MusclePalpation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('masseter_right', models.CharField(max_length=200)),
                ('masseter_left', models.CharField(max_length=200)),
                ('temporalis_right', models.CharField(max_length=200)),
                ('temporalis_left', models.CharField(max_length=200)),
                ('ecm_right', models.CharField(max_length=200)),
                ('ecm_left', models.CharField(max_length=200)),
                ('digastric_right', models.CharField(max_length=200)),
                ('digastric_left', models.CharField(max_length=200)),
                ('occipital_right', models.CharField(max_length=200)),
                ('occipital_left', models.CharField(max_length=200)),
                ('pc_right', models.CharField(max_length=200)),
                ('pc_left', models.CharField(max_length=200)),
                ('trapezius_right', models.CharField(max_length=200)),
                ('trapezius_left', models.CharField(max_length=200)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_profile.patientprofile')),
            ],
        ),
    ]
