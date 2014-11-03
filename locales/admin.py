from django.contrib import admin

from .models import Store


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
