from django.contrib import admin
from .models import Region, Provincia, Comuna, Refugio

admin.site.register(Region)
admin.site.register(Provincia)
admin.site.register(Comuna)

class RefugioAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_registro',)

admin.site.register(Refugio, RefugioAdmin)

