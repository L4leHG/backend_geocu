# Generated by Django 4.0.1 on 2022-04-03 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geovisor', '0013_municipio'),
    ]

    operations = [
        migrations.AddField(
            model_name='predio',
            name='area_cartografica',
            field=models.FloatField(null=True),
        ),
    ]
