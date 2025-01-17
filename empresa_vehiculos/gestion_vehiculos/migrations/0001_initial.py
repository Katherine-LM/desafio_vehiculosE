# Generated by Django 3.2.4 on 2024-06-05 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chofer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('licencia', models.CharField(max_length=100, unique=True)),
                ('habilitado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=100, unique=True)),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('año', models.IntegerField()),
                ('habilitado', models.BooleanField(default=True)),
                ('chofer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestion_vehiculos.chofer')),
            ],
        ),
        migrations.CreateModel(
            name='RegistroContable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalles', models.TextField()),
                ('vehiculo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gestion_vehiculos.vehiculo')),
            ],
        ),
    ]
