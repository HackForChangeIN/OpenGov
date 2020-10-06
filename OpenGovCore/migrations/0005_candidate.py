# Generated by Django 3.1 on 2020-09-16 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OpenGovCore', '0004_sittings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500)),
                ('dob', models.CharField(blank=True, max_length=200)),
                ('qualification', models.CharField(blank=True, max_length=500)),
                ('gender', models.CharField(blank=True, max_length=100)),
                ('social_class', models.CharField(blank=True, max_length=500)),
                ('contact_number', models.CharField(blank=True, max_length=500)),
                ('email', models.CharField(blank=True, max_length=500)),
                ('profession', models.CharField(blank=True, max_length=500)),
                ('criminal_cases', models.CharField(blank=True, max_length=500)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('present_address', models.TextField(blank=True)),
                ('permanent_address', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Candidate',
                'verbose_name_plural': 'Candidates',
            },
        ),
    ]