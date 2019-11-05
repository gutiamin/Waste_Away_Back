# Generated by Django 2.2.7 on 2019-11-05 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('nombre', models.CharField(max_length=200)),
                ('correo', models.EmailField(max_length=254)),
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('contrasenia', models.CharField(max_length=50)),
                ('desperdicio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('edad', models.IntegerField()),
                ('estatura', models.IntegerField()),
                ('peso', models.IntegerField()),
                ('genero', models.CharField(max_length=15)),
                ('condicion_medica', models.CharField(max_length=150)),
                ('alergias', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=10)),
                ('desperdicio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=10)),
                ('desperdicio', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('correo', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.IntegerField()),
                ('contrasenia', models.CharField(max_length=50)),
                ('desperdicio', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
