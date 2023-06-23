# Generated by Django 4.2.2 on 2023-06-23 16:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Asset_Tracker_app", "0015_alter_assetmodel_assetcode_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assetmodel",
            name="AssetCode",
            field=models.TextField(default="e70bb155-3e68-4880"),
        ),
        migrations.AlterField(
            model_name="assetmodel",
            name="Created_At",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 23, 16, 35, 16, 583052)
            ),
        ),
        migrations.AlterField(
            model_name="assetmodel",
            name="Updated_At",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 23, 16, 35, 16, 583064)
            ),
        ),
        migrations.AlterField(
            model_name="assettypemodel",
            name="Created_At",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 23, 16, 35, 16, 582482)
            ),
        ),
        migrations.AlterField(
            model_name="assettypemodel",
            name="Updated_At",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 23, 16, 35, 16, 582497)
            ),
        ),
    ]
