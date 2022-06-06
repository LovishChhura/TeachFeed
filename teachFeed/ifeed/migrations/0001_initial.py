# Generated by Django 4.0.3 on 2022-06-05 14:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Taccess',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('department', models.CharField(help_text='Enter a Department (e.g. IT)', max_length=100, validators=[django.core.validators.MinLengthValidator(2, 'Make must be greater than 1 character')])),
                ('accesscd', models.CharField(max_length=100)),
            ],
        ),
    ]
