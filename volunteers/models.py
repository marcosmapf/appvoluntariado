from django.db import models
from django.template.defaultfilters import slugify

class Volunteer(models.Model):

	GENDER_CHOICES = (('MA', 'MALE'), ('FE', 'FEMALE'), ('NI', 'NOT INFORMED'))
	STATE_CHOICES =  (
		('AC', 'ACRE'), ('Al', 'ALAGOAS'), ('AP', 'AMAPA'), ('AM', 'AMAZONAS'), ('BA', 'BAHIA'), ('CE', 'CEARA'), ('DF', 'DISTRITO FEDERAL'), 
		('ES', 'ESPIRITO SANTO'), ('GO', 'GOIAS'), ('MA', 'MARANHAO'), ('MT', 'MATO GROSSO'), ('MS', 'MATO GROSSO DO SUL'), ('MG', 'MINAS GERAIS'), 
		('PA', 'PARA'), ('PB', 'PARAIBA'), ('PR', 'PARANA'), ('PE', 'PERNAMBUCO'), ('PI', 'PIAUI'), ('RJ', 'RIO DE JANEIRO'), ('RN', 'RIO GRANDE DO NORTE'),
		('RS', 'RIO GRANDE DO SUL'), ('RO', 'RONDONIA'), ('RR', 'RORAIMA'), ('SC', 'SANTA CATARINA'), ('SP', 'SAO PAULO'), ('SE', 'SERGIPE'), ('TO', 'TOCANTINS'),
	)

	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	state = models.CharField(max_length=2, choices=STATE_CHOICES)
	city = models.CharField(max_length=255)
	gender = models.CharField(max_length=2, choices=GENDER_CHOICES, blank=True, null=True)
	phone = models.CharField(max_length=13)	
	email = models.EmailField(max_length=100)
	description = models.TextField(max_length=500)	
	photo = models.ImageField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	interest_areas = models.CharField(max_length=255, blank=True, null=True)
	
	class Meta:
		verbose_name_plural = "Volunteers"

	def __str__(self):
	    return self.first_name + self.last_name

	def get_absolute_url(self):
	    return reverse('volunteers:volunteer-detail', kwargs={'pk': self.id})