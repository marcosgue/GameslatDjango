from django.contrib import admin

from .models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'DNI_CUIT',
        'phone',
        'points'
    )
