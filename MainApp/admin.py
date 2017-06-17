from django.contrib import admin
from .models import Person, Category, Privilege, Avatar, Tag, Photo, News, \
    Request, Location, Order, Portfolio


admin.site.register(Person)
admin.site.register(Category)
admin.site.register(Privilege)
admin.site.register(Avatar)
admin.site.register(Tag)
admin.site.register(Photo)
admin.site.register(News)
admin.site.register(Request)
admin.site.register(Location)
admin.site.register(Order)
admin.site.register(Portfolio)



# Register your models here.
