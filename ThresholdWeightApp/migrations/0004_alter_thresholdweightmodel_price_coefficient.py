# Generated by Django 4.1.1 on 2022-09-28 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ThresholdWeightApp', '0003_alter_thresholdweightmodel_price_coefficient_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thresholdweightmodel',
            name='price_coefficient',
            field=models.FloatField(),
        ),
    ]
