from django.db.models import fields
from django import forms

from .models import Record

class RecordForm(forms.Form):
	content = forms.CharField(label='message', max_length=100)
