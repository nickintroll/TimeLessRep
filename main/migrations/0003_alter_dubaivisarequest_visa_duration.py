# Generated by Django 4.1.3 on 2023-02-17 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_dubaivisarequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dubaivisarequest',
            name='visa_duration',
            field=models.CharField(choices=[('Trourist visa(30 days)', 'Trourist visa(30 days)'), ('Trourist visa(60 days)', 'Trourist visa(60 days)'), ('Multivisa(30 days)', 'Multivisa(30 days)'), ('Multivisa(60 days)', 'Multivisa(60 days)')], default='Trourist visa(30 days)', max_length=120),
        ),
    ]