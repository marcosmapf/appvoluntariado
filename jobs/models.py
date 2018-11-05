from django.db import models
from django.template.defaultfilters import slugify
from companies.models import Company
from volunteers.models import Volunteer
from volunteeringareas.models import VolunteeringArea

class Job(models.Model):

	RECURRENCY_CHOICES = (('OO', 'Somente uma vez'), ('ML', 'Mensalmente'), ('WK', 'Semanalmente'), ('DL', 'Diariamente'))
	STATE_CHOICES =  (
		('AC', 'ACRE'), ('Al', 'ALAGOAS'), ('AP', 'AMAPA'), ('AM', 'AMAZONAS'), ('BA', 'BAHIA'), ('CE', 'CEARA'), ('DF', 'DISTRITO FEDERAL'), 
		('ES', 'ESPIRITO SANTO'), ('GO', 'GOIAS'), ('MA', 'MARANHAO'), ('MT', 'MATO GROSSO'), ('MS', 'MATO GROSSO DO SUL'), ('MG', 'MINAS GERAIS'), 
		('PA', 'PARA'), ('PB', 'PARAIBA'), ('PR', 'PARANA'), ('PE', 'PERNAMBUCO'), ('PI', 'PIAUI'), ('RJ', 'RIO DE JANEIRO'), ('RN', 'RIO GRANDE DO NORTE'),
		('RS', 'RIO GRANDE DO SUL'), ('RO', 'RONDONIA'), ('RR', 'RORAIMA'), ('SC', 'SANTA CATARINA'), ('SP', 'SAO PAULO'), ('SE', 'SERGIPE'), ('TO', 'TOCANTINS'),
	)

	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	description = models.TextField(max_length=510)
	photo = models.ImageField(blank=True, null=True)
	start_date = models.DateTimeField()
	finish_date = models.DateTimeField()
	recurrency = models.CharField(max_length=2, choices=RECURRENCY_CHOICES)
	job_areas = models.ManyToManyField(VolunteeringArea)
	contact_email = models.EmailField(max_length=100)
	state = models.CharField(max_length=2, choices=STATE_CHOICES)
	city = models.CharField(max_length=255)
	neighborhood = models.CharField(max_length=255)
	street = models.CharField(max_length=255)
	street_number = models.CharField(max_length=6)
	extra_location = models.CharField(max_length=100, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	#updated_at = models.DateTimeField()
	expiration_date = models.DateTimeField(auto_now_add=True) #remove auto_now_add later
	is_active = models.BooleanField(default=False)
	
	class Meta:
		verbose_name_plural = "Jobs"

	def __str__(self):
	    return self.title

	def slug(self):
	    return slugify(self.trading_name)	    

	def get_absolute_url(self):
	    return reverse('jobs:job-detail', kwargs={'pk': self.id})



class JobMatch(models.Model):

	company = models.ForeignKey(Company, on_delete=models.CASCADE)		    
	volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
	job_areas = models.ForeignKey(VolunteeringArea)
	attended_job = models.NullBooleanField()
	company_commentary = models.TextField(max_length=510, blank=True)
	volunteer_commentary = models.TextField(max_length=510, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = "Job Matchs"

	def __str__(self):
		return 'Empresa: ' + str(self.company) + '/ Voluntário: ' + str(self.volunteer)

	#def slug(self):
		#return slugify(self.trading_name)	    

	def get_absolute_url(self):
		return reverse('jobs:job-matchs-detail', kwargs={'pk': self.id})	