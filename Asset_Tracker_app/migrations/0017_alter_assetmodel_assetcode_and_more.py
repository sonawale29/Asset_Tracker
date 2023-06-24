# Generated by Django 4.2.2 on 2023-06-24 09:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Asset_Tracker_app", "0016_alter_assetmodel_assetcode_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assetmodel",
            name="AssetCode",
            field=models.TextField(default="6d406b4f-5269-4b2f"),
        ),
        migrations.AlterField(
            model_name="assetmodel",
            name="Created_At",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 24, 9, 5, 5, 22928)
            ),
        ),
        migrations.AlterField(
            model_name="assetmodel",
            name="Updated_At",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 24, 9, 5, 5, 22940)
            ),
        ),
        migrations.AlterField(
            model_name="assettypemodel",
            name="Created_At",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 24, 9, 5, 5, 22359)
            ),
        ),
        migrations.AlterField(
            model_name="assettypemodel",
            name="Updated_At",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 24, 9, 5, 5, 22373)
            ),
        ),
    ]
