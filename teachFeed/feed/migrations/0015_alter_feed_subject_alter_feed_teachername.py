# Generated by Django 4.0.3 on 2022-05-31 04:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0014_feed_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='subject',
            field=models.CharField(help_text='Enter a Subject (e.g. DSA)', max_length=100, null=True, validators=[django.core.validators.MinLengthValidator(2, 'Make must be greater than 1 character')]),
        ),
        migrations.AlterField(
            model_name='feed',
            name='teacherName',
            field=models.CharField(help_text="Enter a Teacher's name", max_length=100, null=True, validators=[django.core.validators.MinLengthValidator(2, 'Make must be greater than 1 character')]),
        ),
    ]
