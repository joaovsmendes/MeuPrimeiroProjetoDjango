# Generated by Django 4.0.5 on 2022-07-05 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rh', '0004_alter_funcionario_departamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='departamento',
            field=models.CharField(max_length=20),
        ),
    ]
