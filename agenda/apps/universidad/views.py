from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index_univ(request):
	return HttpResponse("VISTA de UNIVERSIDAD")