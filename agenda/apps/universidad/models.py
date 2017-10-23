from django.db import models

# Create your models here.
class Universidad(models.Model):
	id_univ = models.CharField(max_length=50, primary_key= True)
	nombre = models.CharField(max_length=50)