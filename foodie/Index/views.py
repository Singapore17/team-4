from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import RedirectView, FormView
from Index.forms import *

class DonationFormSubmission(FormView):
	template_name 	= "DonationForm.html"
	form_class 		= DonationsForms
	success_url 	= '/donation-form-received'

	def form_valid(self, form, *args, **kwargs):
		import IPython
		IPython.embed()
		cleaned_form_dict 	= form.clean()
		# Update DB here
		return super(DonationFormSubmission, self).form_valid(form)

	def form_invalid(self, form):
		return super(DonationFormSubmission, self).form_invalid(form)

class DonationFormSubmissionRedirect(RedirectView):
	permanent 		= False
	query_string 	= True
	pattern_name 	= 'main-page'