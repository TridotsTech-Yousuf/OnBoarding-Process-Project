# Copyright (c) 2025, Mohammed Yousuf and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator

# API 3 - Upside
@frappe.whitelist()
def sleep():
	frappe.msgprint("Sleep")
	return "Sleep"

class Example(WebsiteGenerator):

	# API 1 - Inside Class
	@frappe.whitelist()
	def greet(self):
		frappe.msgprint("Greet")
		return "Greet"
	
# API 2 - Outside
@frappe.whitelist()
def scold():
	frappe.msgprint("Scold")
	return "Scold"

