from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request, 'index.html')

def donor_profile(request):
	return render(request, 'donor_profile.html')
