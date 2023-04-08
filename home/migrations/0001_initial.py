# Generated by Django 4.1.1 on 2023-04-04 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_name', models.CharField(max_length=5)),
                ('IIT_Kanpur', models.CharField(max_length=5)),
                ('Kalyanpur', models.CharField(max_length=5)),
                ('SPM_Hospital', models.CharField(max_length=5)),
                ('Vishwavidyalay', models.CharField(max_length=5)),
                ('Gurudev_Chauraha', models.CharField(max_length=5)),
                ('Geeta_Nagar', models.CharField(max_length=5)),
                ('Rawatpur', models.CharField(max_length=5)),
                ('Lala_Lajpat_Rai_Hospital', models.CharField(max_length=5)),
                ('Motijheel', models.CharField(max_length=5)),
            ],
        ),
    ]