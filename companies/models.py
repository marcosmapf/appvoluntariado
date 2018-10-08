from django.db.models import Q
from django.db import models
from django.template.defaultfilters import slugify

class Company(models.Model):

	trading_name = models.CharField(max_length=100)
	company_sector = models.CharField(max_length=100)
	company_location = models.CharField(max_length=255, null=True, blank=True)
	phone = models.CharField(max_length=13)
	email = models.EmailField(max_length=100)
	website = models.URLField(null=True, blank=True)
	description = models.TextField(max_length=500)
	logo = models.ImageField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	

	class Meta:
		ordering = ("trading_name",)
		verbose_name_plural = "Companies"

	def __str__(self):
	    return self.trading_name

	def get_absolute_url(self):
	    return reverse('companies:company-detail', kwargs={'pk': self.id})

	def slug(self):
	    return slugify(self.trading_name)