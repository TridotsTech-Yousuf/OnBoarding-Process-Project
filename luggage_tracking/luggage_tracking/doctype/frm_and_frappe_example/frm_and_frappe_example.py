# Copyright (c) 2025, Mohammed Yousuf and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class FRMANDFrappeExample(Document):
	# API 1 - Inside Class

	# @staticmethod
	@frappe.whitelist()
	def greet(self, static_name):
		frappe.msgprint(f"Greet Static Name: {static_name}")
		# frappe.msgprint()
		return "Greet"
	
# API 2 - Outside
@frappe.whitelist()
def scold():
	frappe.msgprint("Scold")
	return "Scold"

