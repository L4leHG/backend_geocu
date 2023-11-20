# Generated by Django 4.0.1 on 2022-03-24 02:03

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geovisor', '0010_alter_predio_departamento_alter_predio_destino_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alfa_carto',
            name='terreno',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='geovisor.terreno_zonas'),
        ),
        migrations.AlterField(
            model_name='construcciones',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=4686),
        ),
        migrations.AlterField(
            model_name='resolucion_historica',
            name='comienzo_vida_util',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='resolucion_historica',
            name='fin_vida_util',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='resolucion_predio',
            name='comienzo_vida_util',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='resolucion_predio',
            name='fin_vida_util',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='resolucion_predio',
            name='tipo_resolucion',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='terreno_zonas',
            name='area_digitada',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='terreno_zonas',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=4686),
        ),
        migrations.AlterField(
            model_name='terreno_zonas',
            name='zhf',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='terreno_zonas',
            name='zhg',
            field=models.IntegerField(null=True),
        ),
    ]
