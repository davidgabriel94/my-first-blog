from django.db import models

# Create your models here.
class Usuarios(models.Model):
	username = models.CharField(max_length=50)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	password1 = models.CharField(max_length=50)
	password2 = models.CharField(max_length=50)
#class Alumno(models.Model):
#	nombre = models.CharField (max_length=50)
	#direccion = models.TextField(max_length=50)
	#telefono = models.CharField(max_length=50)
	#codigo_postal = models.CharField(max_length=6)
	#email = models.EmailField(max_length=50)
	#fecha_naci = models.DateField()