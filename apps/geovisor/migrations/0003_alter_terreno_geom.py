# Generated by Django 4.0.1 on 2022-03-23 19:22

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geovisor', '0002_alter_terreno_area_digitada_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terreno',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=4686),
        ),
    ]
