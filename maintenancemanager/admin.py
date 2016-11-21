from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Client)
admin.site.register(ClientType)
admin.site.register(Vehicle)
admin.site.register(Service)
admin.site.register(ServiceTransaction)
admin.site.register(Shop)
admin.site.register(ShopService)
admin.site.register(DataChangeLog)
admin.site.register(Ownership)
