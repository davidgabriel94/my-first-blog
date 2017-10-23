from django import forms
 class AlumnoForm(forms.ModelForm):
 	class meta:
 		model = Alumno

 		fields{
	'nombre',
	'direccion',
	'telefono',
	'codigo_postal',
	'email',
	'fecha_naci',
	'universidad',
 		}
 		labels{
	'nombre': 'NOMBRE'
	'direccion': 'DIRECCION'
	'telefono': 'TELEFONO'
	'codigo_postal': 'CODIGO_POSTAL'
	'email':'EMAIL'
	'fecha_naci':'FECHA_NACIMIENTO'
	'universidad': 'UNIVERSIDAD'

 		}