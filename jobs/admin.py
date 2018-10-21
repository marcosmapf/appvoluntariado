from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
	list_display = (
		'id',
	    'title',
	 	'company',
	    'start_date',
	    'finish_date',
	    'recurrency',
	    'state',
	    'contact_email',
	)
	list_filter = (
	    'recurrency',
	    'state',
	    'company',
	)
	
	search_fields = ('title', 'state', 'contact_email')
	readonly_fields = ('created_at', )