from django.contrib import admin

from .models import Store, Puesto


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = (
        'store_name',
        'phone',
        'email',
        'DNI_CUIT',
        'points',
        'logo_img',
    )


@admin.register(Puesto)
class PuestoAdmin(admin.ModelAdmin):
    list_display = (
        'puesto',
    )
