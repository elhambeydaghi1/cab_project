# Generated by Django 4.1.1 on 2022-09-27 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ThresholdWeightApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThresholdWeightModel',
            fields=[
                ('requests_threshold', models.IntegerField(max_length=15, primary_key=True, serialize=False)),
                ('price_coefficient', models.IntegerField(max_length=5)),
            ],
        ),
        migrations.DeleteModel(
            name='PriceWeightModel',
        ),
    ]
