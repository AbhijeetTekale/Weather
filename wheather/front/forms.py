from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = "Date"

class Dat(forms.ModelForm):
    Date = forms.CharField(widget=DateInput, max_length=10)
