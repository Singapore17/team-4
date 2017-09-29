from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import RedirectView, FormView
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from Index.forms import *
from DbController.views import *
from DbController.models import *
from datetime import datetime
import json

@method_decorator(csrf_exempt, name='dispatch')
class DonationFormSubmission(View):
	def get(self, request, *args, **kwargs):
		context 	= {}
		return render(request, "DonationForm.html", context)

	def post(self, request, *args, **kwargs):
		data 		= json.loads(request.body.decode('utf-8'))
		
		# Update item stock count
		DbStockCountController.add("baby_milk_powder", int(data["baby_milk_powder"]))
		DbStockCountController.add("chicken", int(data["chicken"]))
		DbStockCountController.add("tuna_and_beans", int(data["tuna_and_beans"]))

		# Update donation table
		donor_ref 	= DbDonorsController.get(data['ORGANISATION'])
		DbDonationsController.add(donor_ref, ItemTable.objects.all()[0], int(data['baby_milk_powder']))
		DbDonationsController.add(donor_ref, ItemTable.objects.all()[1], int(data['chicken']))
		DbDonationsController.add(donor_ref, ItemTable.objects.all()[2], int(data['tuna_and_beans']))
		return HttpResponse("ok")

class DonationFormSubmissionRedirect(RedirectView):
	permanent 		= False
	query_string 	= True
	pattern_name 	= 'main-page'	