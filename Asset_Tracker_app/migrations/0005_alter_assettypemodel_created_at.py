# Generated by Django 4.2.2 on 2023-06-23 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asset_Tracker_app', '0004_assetmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assettypemodel',
            name='Created_At',
            field=models.DateField(default='Fri Jun 23 05:27:45 2023'),
        ),
    ]
