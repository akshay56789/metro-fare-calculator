# Generated by Django 4.1.1 on 2023-04-04 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fare',
            name='station_name',
            field=models.CharField(max_length=30),
        ),
    ]