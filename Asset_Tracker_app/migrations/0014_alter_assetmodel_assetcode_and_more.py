# Generated by Django 4.2.2 on 2023-06-23 10:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asset_Tracker_app', '0013_alter_assetmodel_assetcode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetmodel',
            name='AssetCode',
            field=models.TextField(default='33edab0f-84ed-440a'),
        ),
        migrations.AlterField(
            model_name='assetmodel',
            name='Created_At',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 23, 10, 54, 15, 411205)),
        ),
        migrations.AlterField(
            model_name='assetmodel',
            name='Updated_At',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 23, 10, 54, 15, 411218)),
        ),
        migrations.AlterField(
            model_name='assettypemodel',
            name='Created_At',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 23, 10, 54, 15, 410740)),
        ),
        migrations.AlterField(
            model_name='assettypemodel',
            name='Updated_At',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 23, 10, 54, 15, 410755)),
        ),
    ]
