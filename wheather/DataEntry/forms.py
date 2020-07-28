from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = "Date"

class Details(forms.ModelForm):
    parameter1 = forms.CharField(widget=forms.TextInput, max_length=10)
    parameter2 = forms.CharField(widget=forms.TextInput, max_length=10)
    parameter3 = forms.CharField(widget=forms.TextInput, max_length=10)
    parameter4 = forms.CharField(widget=forms.TextInput, max_length=10)
    parameter5 = forms.CharField(widget=forms.TextInput, max_length=10)
    parameter6 = forms.CharField(widget=forms.TextInput, max_length=10)
    parameter7 = forms.CharField(widget=forms.TextInput, max_length=10)
    parameter8 = forms.CharField(widget=forms.TextInput, max_length=10)
    Date       = forms.CharField(widget=DateInput, max_length=10)
    Time       = forms.CharField(widget=forms.TextInput, max_length=10)

    class Meta():
        model = Test
        fields = ['parameter1','parameter2','parameter3','parameter4','parameter5','parameter6','parameter7','parameter8','Date','Time']
