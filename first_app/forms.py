from django import forms
from .models import *


class Statechoicefield(forms.Form):
	states = forms.ModelChoiceField(queryset=Trailfam.objects.values_list("state", flat=True).distinct(), empty_label=None)

