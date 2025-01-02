# Copyright (c) 2024, Quantbit Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class EmployeeBonusPayroll(Document):
	
	# def on_submit(self):
	# 	if self.start_date and self.end_date and self.payroll_entry:
	# 		dc = self.payroll_entry
	# 		dc.flags.ignore_validate = True
	# 		dc.submit()
 
 
	def on_submit(self):
		if self.start_date and self.end_date and self.payroll_entry:
			try:
				dc = frappe.get_doc("Payroll Entry", self.payroll_entry)

				if dc.docstatus == 0:
					dc.flags.ignore_validate = True
					dc.submit()
				else:
					frappe.msgprint(f"The Payroll Entry {self.payroll_entry} is already submitted.")
			except Exception as e:
				frappe.throw(f"An error occurred while submitting Payroll Entry: {e}")