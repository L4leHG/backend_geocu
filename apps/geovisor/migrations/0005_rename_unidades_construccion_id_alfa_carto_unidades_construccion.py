# Generated by Django 4.0.1 on 2022-03-23 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geovisor', '0004_remove_unidades_construccion_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alfa_carto',
            old_name='unidades_construccion_id',
            new_name='unidades_construccion',
        ),
    ]
