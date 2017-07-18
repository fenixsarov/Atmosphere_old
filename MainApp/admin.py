from django.contrib import admin
from .models import *


class ReformatAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Request._meta.fields]
    list_filter = ["name"]
    search_fields = list_display

    class Meta:
        model = Request


admin.site.register(Person)
admin.site.register(Category)
admin.site.register(Privilege)
admin.site.register(Avatar)
admin.site.register(Tag)
admin.site.register(Photo)
admin.site.register(News)
admin.site.register(Request, ReformatAdmin)
admin.site.register(Location)
admin.site.register(Order)
admin.site.register(Portfolio)



# Register your models here.
