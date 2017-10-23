from django.db import models
from apps.universidad.models import Universidad
# Create your models here.

class Alumno(models.Model):
	nombre = models.CharField(max_length=50)
	direccion = models.TextField(max_length=50)
	telefono = models.CharField(max_length=50)
	codigo_postal = models.CharField(max_length=6)
	email = models.EmailField(max_length=50)
	fecha_naci = models.DateField()
	
	universidad = models.ForeignKey(Universidad, null=True, blank= True, on_delete=models.CASCADE)