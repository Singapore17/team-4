from django.shortcuts import render
from DbController.models import *

class DbAllocationController(object):
	def create(self):
		pass

class DbDonorsController(object):
	def create(self):
		pass

class DbDonationsController(object):
	def create(self):
		pass

class DbStockCountController(object):
	def add(self, item_name, qty):
		item_set 			= StockCountTable.objects.filter(item__name=item_name).first()
		item_set.quantity 	+= qty
		item_set.save()
		return

	def get(self, item_name):
		item_set 			= StockCountTable.objects.filter(item__name=item_name).first()
		return item_set.quantity

class DbBeneficiariesController(object):
	def create(self):
		pass