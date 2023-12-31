# Generated by Django 4.0.1 on 2022-03-23 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geovisor', '0008_alter_unidades_identificador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alfa_carto',
            name='npn',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='alfa_carto',
            name='predio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='geovisor.predio'),
        ),
        migrations.AlterField(
            model_name='alfa_carto',
            name='terreno',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='geovisor.terreno'),
        ),
        migrations.AlterField(
            model_name='alfa_carto',
            name='unidades_construccion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='geovisor.unidades'),
        ),
    ]
