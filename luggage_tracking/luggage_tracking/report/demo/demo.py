# Copyright (c) 2025, Mohammed Yousuf and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns, data = [], []

	
	columns = [
		{
			"fieldname":"passenger_name",
			"label": "Passenger Name",
			"fieldtype": "Data",
		},
		{
			"fieldname":"is_verified",
			"label": "Is Verified",
			"fieldtype": "Check",
		}
	]

	
	data = frappe.get_all(
		doctype="Passenger Verification",
		fields = ["passenger_name","is_verified"],
	)

	return columns, data











































