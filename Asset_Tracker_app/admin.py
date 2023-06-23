from django.contrib import admin
from Asset_Tracker_app.models import AssetTypeModel,AssetModel

# Register your models here.
admin.site.register(AssetTypeModel)
admin.site.register(AssetModel)