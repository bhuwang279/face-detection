# Generated by Django 2.2.11 on 2020-03-23 14:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200323_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeredfaces',
            name='image_encoding',
            field=models.BinaryField( max_length=900000),
            preserve_default=False,
        ),
    ]
