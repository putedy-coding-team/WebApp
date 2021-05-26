from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.BaoNumber)
admin.site.register(models.PublicInformation)
admin.site.register(models.MaintainEvent)
admin.site.register(models.MaintainInformation)
admin.site.register(models.Hardware)
