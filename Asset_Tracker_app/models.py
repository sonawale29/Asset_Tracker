from django.db import models
from datetime import datetime
import uuid  # This module used for generate unique ID for the Asset


def generate_asset_code(random_value):
    """This function create the Unique ID for the Asset Type"""
    asset_code = random_value.split("-")
    return "-".join(asset_code[:3])


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
    AssetType = models.ForeignKey(AssetTypeModel, on_delete=models.CASCADE) # Relationship establish between the Asset
    # type and Asset i.e one-many relation using ORM.
    Created_At = models.DateTimeField(default=datetime.now())
    Updated_At = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.AssetCode
