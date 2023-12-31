# Generated by Django 4.2.2 on 2023-06-30 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avocado_Prices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('average_price', models.FloatField()),
                ('total_volume', models.FloatField()),
                ('avocado_4046', models.FloatField()),
                ('avocado_4225', models.FloatField()),
                ('avocado_4770', models.FloatField()),
                ('total_bags', models.FloatField()),
                ('small_bags', models.FloatField()),
                ('large_bags', models.FloatField()),
                ('xlarge_bags', models.FloatField()),
                ('avocado_type', models.CharField(max_length=60)),
                ('region', models.CharField(max_length=60)),
            ],
        ),
    ]
