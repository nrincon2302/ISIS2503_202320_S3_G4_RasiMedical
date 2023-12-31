# Generated by Django 3.2.6 on 2023-09-29 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('especialidad', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=50)),
                ('edad', models.IntegerField()),
            ],
        ),
    ]
