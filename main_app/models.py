from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Disease(models.Model):
	name = models.CharField(max_length = 30)
	pain = models.CharField(max_length = 30)
	cure = models.CharField(max_length = 100)
	survivability = models.IntegerField()

	def __str__(self):
                return(self.name)

		
