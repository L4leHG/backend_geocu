# Generated by Django 4.0.1 on 2022-03-23 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geovisor', '0007_alter_unidades_avaluo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unidades',
            name='identificador',
            field=models.TextField(null=True),
        ),
    ]
