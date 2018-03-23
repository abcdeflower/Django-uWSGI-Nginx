from django.db import models

# Create your models here.
class Guest(models.Model):
	name=models.CharField(max_length=30)
	token=models.CharField(max_length=30)
	pwd=models.CharField(max_length=30)
	def __string__(self):
		return self.name
