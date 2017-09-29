from django import forms

class DonationsForms(forms.Form):
	name 			= forms.CharField(max_length=100)
	contact_name 	= forms.CharField(max_length=100)
	contact_no 		= forms.CharField(max_length=20)
	email 			= forms.EmailField(max_length=150)
	
	item_A 			= forms.IntegerField()
	item_B 			= forms.IntegerField()
	item_C 			= forms.IntegerField()