from django.contrib import admin

from consumer import models

admin.site.register(models.Consumer)
admin.site.register(models.DiscountRules)
