from django.contrib import admin
from .models import VolunteeringArea

@admin.register(VolunteeringArea)
class VolunteeringAreaAdmin(admin.ModelAdmin):
	list_display = (
		'id',
	    'title',
	    'description',
	    'created_at',
	    'is_active'
	)
	list_filter = (
	    'is_active',
	)	
	search_fields = ('title',)
	readonly_fields = ('created_at', )