from django.db import models

# Create your models here.
class login (models.Model):
	email=models.CharField(max_length=70,default="")
	password=models.CharField(max_length=30,default="")
	def __str__(self):
		return self.email[0:12]	

