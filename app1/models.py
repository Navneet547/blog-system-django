from django.db import models

# Create your models here.
class blogmodel(models.Model):
	ids=models.IntegerField()
	title=models.CharField(max_length=100)
	body=models.CharField(max_length=200)

	def __str__(self):
		return self.title