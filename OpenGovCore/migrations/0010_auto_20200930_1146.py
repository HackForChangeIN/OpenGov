# Generated by Django 3.1 on 2020-09-30 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OpenGovCore', '0009_debates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assembly_constituencies',
            name='constituency_number',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
