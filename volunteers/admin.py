from django.contrib import admin
from .models import Volunteer

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = (
    	'id',
        'first_name',
        'last_name',
        'state',
        'city',
        'phone',
        'email',
        'created_at'
    )

    list_filter = (
        'state',
        'city'
    )

    search_fields = ('first_name', 'last_name', 'email', 'state', 'city')
    readonly_fields = ('created_at', )