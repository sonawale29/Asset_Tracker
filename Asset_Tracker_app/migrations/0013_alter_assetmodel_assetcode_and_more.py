# Generated by Django 4.2.2 on 2023-06-23 08:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asset_Tracker_app', '0012_alter_assetmodel_assetcode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetmodel',
            name='AssetCode',
            field=models.TextField(default='00d558ab-97ef-4c2d'),
        ),
        migrations.AlterField(
            model_name='assetmodel',
            name='Created_At',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 23, 8, 9, 18, 15423)),
        ),
        migrations.AlterField(
            model_name='assetmodel',
            name='Updated_At',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 23, 8, 9, 18, 15439)),
        ),
        migrations.AlterField(
            model_name='assettypemodel',
            name='Created_At',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 23, 8, 9, 18, 14985)),
        ),
        migrations.AlterField(
            model_name='assettypemodel',
            name='Updated_At',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 23, 8, 9, 18, 15000)),
        ),
    ]
