# Generated by Django 3.2.7 on 2021-10-31 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pain_mapping', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='painmapping',
            name='note',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
