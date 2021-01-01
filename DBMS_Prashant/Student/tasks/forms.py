from django import forms
from django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm):
	usn = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Enter Your USN'}))
	Name = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Enter Your Name'}))
	Platform = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Course Platform'}))
	Course = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Enter Course Name'}))

	class Meta:
		model = Task
		fields = '__all__'