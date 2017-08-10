from django.contrib import admin
from django.apps import apps
from .models import *


class RequestInOrderInline(admin.TabularInline):
    model = RequestInOrder
    extra = 0


for model in apps.get_app_config('Orders').models.values():
    class ReformatAdmin(admin.ModelAdmin):
        list_display = [field.name for field in model._meta.fields]
        if model.__name__ == 'Order': inlines = [RequestInOrderInline]

        class Meta:
            model = model


    admin.site.register(model, ReformatAdmin)


# Register your models here.
