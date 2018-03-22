from django.db import models

# Create your models here.
class Pubulisher(models.Model):
	name=models.CharField(max_length=30)
	address=models.CharField(max_length=50)
	city=models.CharField(max_length=60)
	state_province=models.CharField(max_length=30)
	country=models.CharField(max_length=50)
	website=models.URLField()
	def __str__(self):
		return self.name

class Author(models.Model):
	salutation=models.CharField(max_length=10)
	first_name=models.CharField(max_length=30)
	last_name=models.CharField(max_length=40)
	email=models.EmailField()
	headshot=models.ImageField(upload_to='tmp')
	
	class Admin:
		pass

class Book(models.Model):
	title=models.CharField(max_length=100)
	authors=models.ManyToManyField(Author)
	publisher=models.ForeignKey(Pubulisher,on_delete=models.CASCADE)
	publication_date=models.DateField()
	num_pages=models.IntegerField(blank=True,null=True)
	def __str__(self):
		return self.title

	class Admin:
		list_display=('title','publisher','publication_date')
		list_filter=('publisher','publication_date')	
		orderint=('-publication_date',)
		search_fields=('title',)
