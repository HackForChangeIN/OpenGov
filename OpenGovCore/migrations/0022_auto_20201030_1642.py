# Generated by Django 3.1 on 2020-10-30 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OpenGovCore', '0021_auto_20201030_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bills',
            name='date_of_introduction',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='debates',
            name='date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='date',
            field=models.DateField(blank=True),
        ),
    ]
