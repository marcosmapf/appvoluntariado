from django.db import models

class VolunteeringArea(models.Model):

	title = models.CharField(max_length=100)
	description = models.TextField(max_length=512)
	created_at = models.DateTimeField(auto_now_add=True)
	is_active = models.BooleanField(default=False)

	class Meta:
		verbose_name_plural = "VolunteeringAreas"

	def __str__(self):
	    return self.title

	def slug(self):
	    return slugify(self.title)    