# Generated by Django 3.1 on 2020-10-03 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OpenGovCore', '0012_candidate_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='link',
            new_name='source',
        ),
    ]