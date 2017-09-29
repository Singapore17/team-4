from django.db import models

class ItemTable(models.Model):
	name 			= models.CharField(max_length=100)

	def __str__(self):
		return "Item - {0}".format(self.name)

class BeneficiariesTable(models.Model):
	name 		= models.CharField(max_length=100)
	email 		= models.EmailField(max_length=200)
	size 		= models.IntegerField()
	priority 	= models.IntegerField()

	def __str__(self):
		return "Beneficiaries - {0}".format(self.name)

class DonorsTable(models.Model):
	name 		= models.CharField(max_length=100)
	email 		= models.EmailField(max_length=200)
	contact 	= models.CharField(max_length=20)

	def __str__(self):
		return "Donors - {0}".format(self.name)

class AllocationTable(models.Model):
	item_id 		= models.ForeignKey(ItemTable, on_delete=models.CASCADE)
	beneficiaries 	= models.ForeignKey(BeneficiariesTable, on_delete=models.CASCADE)
	quantitiy 		= models.IntegerField()
	time 			= models.DateTimeField(auto_now=True)

	def __str__(self):
		return "Allocation - {0}".format(self.beneficiaries.name)

class DonationsTable(models.Model):
	donor_id 	= models.ForeignKey(DonorsTable, on_delete=models.CASCADE)
	item_id 	= models.ForeignKey(ItemTable, on_delete=models.CASCADE)
	item_qty 	= models.IntegerField()
	expiry 		= models.DateTimeField(auto_now=True)

	def __str__(self):
		return "Donations - {0}".format(self.donor_id.name)

class StockCountTable(models.Model):
	item 		= models.ForeignKey(ItemTable, on_delete=models.CASCADE)
	quantity 	= models.IntegerField(default=0)

	def __str__(self):
		return "Inventory - {0} - {1}".format(self.item.name, self.quantity)