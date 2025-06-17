// Copyright (c) 2025, Mohammed Yousuf and contributors
// For license information, please see license.txt

frappe.query_reports["Passengers List"] = {
	"filters": [
		{
			"fieldname": "passenger_name",
			"label": __("Passenger Name"),
			"fieldtype": "Data",
		},
		{
			"fieldname": "is_verified",
			"label": __("Is Verified"),
			"fieldtype": "Check",
		}
	]
};
