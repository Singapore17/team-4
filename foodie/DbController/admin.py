from django.contrib import admin
from DbController.models import *

@admin.register(ItemTable)
class ItemTableAdmin(admin.ModelAdmin):
	pass

@admin.register(BeneficiariesTable)
class BeneficiariesTableAdmin(admin.ModelAdmin):
	pass

@admin.register(DonorsTable)
class DonorsTableAdmin(admin.ModelAdmin):
	pass

@admin.register(AllocationTable)
class AllocationTableAdmin(admin.ModelAdmin):
	pass

@admin.register(DonationsTable)
class DonationsTableAdmin(admin.ModelAdmin):
	pass

@admin.register(StockCountTable)
class StockCountTableAdmin(admin.ModelAdmin):
	pass
