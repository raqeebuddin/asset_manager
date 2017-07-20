from django.shortcuts import render
from ams.models import *

# Create your views here.
def index(request):
	return render(request, 'ams/index.html')

def leaptopsearch_view(request):
	return render(request, 'ams/laptopsearch.html')