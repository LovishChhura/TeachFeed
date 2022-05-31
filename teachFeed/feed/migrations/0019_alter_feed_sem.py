# Generated by Django 4.0.3 on 2022-05-31 05:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0018_alter_feed_sem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='sem',
            field=models.CharField(help_text='Enter a Sem (e.g. 1st)', max_length=100, validators=[django.core.validators.MinLengthValidator(2, 'Make must be greater than 1 character')]),
        ),
    ]
