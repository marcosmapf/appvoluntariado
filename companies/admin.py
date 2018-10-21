from django.contrib import admin

from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'trading_name',
        'company_sector',
        'company_location',
        'phone',
        'email',
        'website',
    )

    list_filter = (
        'trading_name',
        'company_sector',
    )

    search_fields = ('trading_name', 'company_sector', 'email')

    readonly_fields = ('created_at',)