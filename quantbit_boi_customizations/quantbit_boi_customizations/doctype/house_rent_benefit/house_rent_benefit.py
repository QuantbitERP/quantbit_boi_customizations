# Copyright (c) 2024, Quantbit Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class HouseRentBenefit(Document):
	

	def calculate_total(self, child_table, total_field,condition_field):
		return sum(getattr(i, total_field) for i in self.get(child_table, {condition_field:['not in', [None , 0]]}))
	

	@frappe.whitelist()
	def calculate_house_rent_total(self):
		for i in self.get("benifit_details",{"amount":['not in' ,[None,0]],"rate":['not in' ,[None, 0]]}):
			i.total = i.amount * i.rate

		self.total_amount = self.calculate_total(child_table="benifit_details",total_field="total",condition_field= "total")
		self.calculate_house_rent()
  
	@frappe.whitelist()
	def calculate_house_rent(self):
		for i in self.get("benifit_details",{"total":['not in' ,[None,0]],"duration":['not in' ,[None, 0]]}):
			i.amount_monthly = (i.total) / i.duration
		self.amount_per_month =self.calculate_total(child_table="benifit_details",total_field="amount_monthly",condition_field= "amount_monthly")