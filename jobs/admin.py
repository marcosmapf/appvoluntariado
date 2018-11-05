from django.contrib import admin
from .models import Job, JobMatch

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


@admin.register(JobMatch)
class JobMatchAdmin(admin.ModelAdmin):
	list_display = (
		'company',
	    'volunteer',
	 	'job_areas',
	    'attended_job',
	    'created_at',
	)
	list_filter = (
	    'company',
	)
	
	search_fields = ('company', 'volunteer')
	readonly_fields = ('created_at', )