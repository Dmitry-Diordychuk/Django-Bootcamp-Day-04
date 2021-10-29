import logging

from django import forms
from django.shortcuts import redirect, render
from .models import Record

from .forms import RecordForm

from datetime import datetime

logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
	records = Record.objects.order_by('-published')

	if request.method == "POST":
		form = RecordForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.post = records
			obj.save()

			logger.info('[' + str(datetime.now()) + ']' + ' ' + obj.content)

			return redirect('index')
	else:
		form = RecordForm()

	context = {
		'records': records,
		'form': form
	}
	return render(request, 'ex02/index.html', context)
