# Copyright (c) 2024, Quantbit Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _

class KeyAllowanceRate(Document):
	# File: key_allowance_rate.py (Server-Side Python Script)



	def validate(self):
		# Check for overlapping date ranges in the Key Allowance Rate doctype
		overlapping_records = frappe.db.sql("""
			SELECT name, from_date, to_date 
			FROM `tabKey Allowance Rate`
			WHERE 
				name != %(name)s AND 
				(
					(%(from_date)s BETWEEN from_date AND to_date) OR
					(%(to_date)s BETWEEN from_date AND to_date) OR
					(from_date BETWEEN %(from_date)s AND %(to_date)s) OR
					(to_date BETWEEN %(from_date)s AND %(to_date)s)
				)
		""", {
			"name": self.name or "",
			"from_date": self.from_date,
			"to_date": self.to_date
		}, as_dict=True)

		# Raise an error if overlapping records are found
		if overlapping_records:
			overlapping_doc = overlapping_records[0]
			frappe.throw(_(
				f"Date range overlaps with an existing record: {overlapping_doc['name']} "
				f"({overlapping_doc['from_date']} to {overlapping_doc['to_date']})."
			))
