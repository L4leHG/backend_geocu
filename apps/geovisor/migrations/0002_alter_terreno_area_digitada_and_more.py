# Generated by Django 4.0.1 on 2022-03-23 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geovisor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terreno',
            name='area_digitada',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='terreno',
            name='comienzo_vida_util',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='terreno',
            name='fin_vida_util',
            field=models.DateField(null=True),
        ),
    ]