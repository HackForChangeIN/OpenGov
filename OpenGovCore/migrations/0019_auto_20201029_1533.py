# Generated by Django 3.1 on 2020-10-29 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OpenGovCore', '0018_auto_20201014_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='source',
            field=models.URLField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='bills',
            name='source',
            field=models.URLField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='source',
            field=models.URLField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='debates',
            name='source',
            field=models.URLField(blank=True, max_length=400),
        ),
    ]
