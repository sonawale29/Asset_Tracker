from django.db import models
from datetime import datetime
import uuid


def generate_asset_code(random_value):
    asset_code = random_value.split('-')
    return "-".join(asset_code[:3])





# Create your models here.


class AssetTypeModel(models.Model):
    Asset_Type = models.TextField()

    Asset_Description = models.TextField(max_length=500)
    Created_At = models.DateTimeField(default=datetime.now())
    Updated_At = models.DateTimeField(default=datetime.now())

    def __str__(self):

        return self.Asset_Type


class AssetModel(models.Model):
    AssetName = models.TextField()
    AssetCode = models.TextField(default=generate_asset_code(str(uuid.uuid4())))
    AssetType = models.ForeignKey(AssetTypeModel,on_delete=models.CASCADE)
    Created_At = models.DateTimeField(default=datetime.now())
    Updated_At = models.DateTimeField(default=datetime.now())

    def __str__(self):

        return self.AssetCode
