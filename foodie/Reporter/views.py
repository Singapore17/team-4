from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from DbController.views import *

class SendEmailToBenefactors(View):
	def get(self, request, *args, **kwargs):
		email_lst 	= DbBeneficiariesController.getAllEmails()
		template 	= None 	# Email template implementation here
		return HttpResponse("Ok")