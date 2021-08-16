from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(Kiosk)
admin.site.register(Employee)
admin.site.register(Stock)
admin.site.register(Sale)


admin.site.site_header = "KIOSK ADMIN"
admin.site.site_title = "KIOSK ADMIN"