from django.shortcuts import render
from DbController.models import *

class DbAllocationController(object):
	@classmethod
	def create(cls):
		pass

class DbDonorsController(object):
	@classmethod
	def create(cls):
		pass

class DbDonationsController(object):
	@classmethod
	def get(cls, donor_name):
		donor_set 				= DonationsTable.objects.filter(donor_id__name=donor_name)
		return_dict 			= {}
		for each_set in donor_set:
			item_name 			= each_set.item_id.name 
			if(return_dict.get(item_name)):
				return_dict[item_name] 	+= each_set.item_qty
			else:
				return_dict[item_name] 	= each_set.item_qty
		return

class DbStockCountController(object):
	@classmethod
	def add(cls, item_name, qty):
		item_set 			= StockCountTable.objects.filter(item__name=item_name).first()
		item_set.quantity 	+= qty
		item_set.save()
		return

	@classmethod
	def less(cls, item_name, qty):
		item_set 			= StockCountTable.objects.filter(item__name=item_name).first()
		item_set.quantity 	-= qty
		item_set.quantity 	= max(item_set.quantity, 0)
		item_set.save()
		return

	@classmethod
	def get(cls, item_name):
		item_set 			= StockCountTable.objects.filter(item__name=item_name).first()
		return item_set.quantity

class DbBeneficiariesController(object):
	@classmethod
	def getAllEmails(cls):
		beneficiaries_set	= BeneficiariesTable.objects.all()
		email 				= []
		for each_beneficiary in beneficiaries_set:
			email.append(each_beneficiary.email)
		return email