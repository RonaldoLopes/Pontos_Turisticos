# Generated by Django 3.2.7 on 2021-09-25 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0001_initial'),
        ('core', '0004_remove_pontoturistico_atracoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='atracao',
            field=models.ManyToManyField(to='atracoes.Atracao'),
        ),
    ]
