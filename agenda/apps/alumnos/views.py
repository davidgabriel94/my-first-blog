from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def alumno_list(request):
	return render(request, 'alumno/index.html')