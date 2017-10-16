from django.contrib import admin
from MainApp.models import *
from django.apps import apps


class ReformatAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Request._meta.fields]
    list_filter = ["name"]
    search_fields = list_display

    class Meta:
        model = Request


for model in apps.get_app_config('MainApp').models.values():
    if model.__name__ == 'Request':
        admin.site.register(model, ReformatAdmin)
    else:
        admin.site.register(model)


# Register your models here.
