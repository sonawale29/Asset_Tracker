# Generated by Django 4.2.2 on 2023-06-23 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asset_Tracker_app', '0002_alter_asset_type_model_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetTypeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Asset_Type', models.TextField()),
                ('Asset_Description', models.TextField(max_length=500)),
                ('Created_At', models.DateTimeField()),
                ('Updated_At', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='Asset_Type_Model',
        ),
    ]
