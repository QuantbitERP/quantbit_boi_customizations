# Copyright (c) 2025, Quantbit Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class WaterCharges(Document):
	
	def calculate_total(self, child_table, total_field,condition_field):
		return sum(getattr(i, total_field) for i in self.get(child_table, {condition_field:['not in', [None , 0]]}))
	

	@frappe.whitelist()
	def calculate_charges(self):
		for i in self.get("charges_details",{"bill_submitted":['not in' ,[None,0]],"rate":['not in' ,[None, 0]]}):
			i.eligible_amount = i.bill_submitted
			if i.eligible_amount:
				i.gross_amount = i.eligible_amount * i.rate
				i.credit_amount = i.eligible_amount
				i.paye = i.gross_amount - i.credit_amount if i.gross_amount else 0

		self.total_paye = self.calculate_total(child_table="charges_details",total_field="paye",condition_field= "paye")