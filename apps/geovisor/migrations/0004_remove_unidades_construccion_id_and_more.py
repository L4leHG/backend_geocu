# Generated by Django 4.0.1 on 2022-03-23 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geovisor', '0003_alter_terreno_geom'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unidades',
            name='construccion_id',
        ),
        migrations.AddField(
            model_name='construcciones',
            name='unidades',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='geovisor.unidades'),
        ),
    ]
