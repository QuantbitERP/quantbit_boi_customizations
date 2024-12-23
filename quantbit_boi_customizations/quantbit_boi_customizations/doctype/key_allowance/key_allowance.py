# Copyright (c) 2024, Quantbit Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import date_diff, today
from frappe.model.mapper import get_mapped_doc
class KeyAllowance(Document):
    
	def calculate_total(self, child_table, total_field,condition_field):
		return sum(getattr(i, total_field) for i in self.get(child_table, {condition_field:['not in', [None , 0]]}))
	
	@frappe.whitelist()
	def calculate_total_days(self):
		for i in self.get("key_details"):
			if i.from_date and i.to_date:
				start_date = i.from_date
				end_date = i.to_date
				if start_date > end_date:
					frappe.throw("From Date cannot be after To Date.")
		
				total_days = date_diff(end_date, start_date)
				i.total_days = total_days

    
    
		self.total_days = self.calculate_total(child_table="key_details",total_field="total_days",condition_field= "total_days")
		self.amount = self.total_days * self.rate if self.total_days and self.rate else 0
  
  
@frappe.whitelist()
def make_additional_salary(source_name,target_doc = None):

	doclist = get_mapped_doc(
		"Key Allowance",
				source_name,
		{
				"Key Allowance":{
					"doctype": "Additional Salary",
				"field_map":{
								"approval_date":"payroll_date",
								"employee":"employee",
								"amount":"amount",
								"company":"company",
								"salary_component":"salary_component",
								"name":"custom_key_allowance"
							},
				},
		}
		)
	return doclist