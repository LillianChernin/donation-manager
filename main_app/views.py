from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ReliefEffortForm

# Create your views here.

def index(request):
    form = ReliefEffortForm()
    return render(request, 'index.html', {'form': form})

    
def post_relief_effort(request):
    form = ReliefEffortForm(request.POST)
    if form.is_valid():
        relief_effort = ReliefEffort(
            name=form.cleaned_data['name'],
            desc=form.cleaned_data['desc'],
            location=form.cleaned_data['location']
        )
        relief_effort.save()
    return HttpResponseRedirect('/')
