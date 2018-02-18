from django import forms
from .models import ReliefEffort

class ReliefEffortForm(forms.ModelForm):
    class Meta:
        model = ReliefEffort
        fields = ['name','desc','location']
