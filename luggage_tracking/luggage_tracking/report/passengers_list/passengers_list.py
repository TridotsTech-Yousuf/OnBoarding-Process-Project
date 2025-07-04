# Copyright (c) 2025, Mohammed Yousuf and contributors
# For license information, please see license.txt
# message = "This report shows the current verification status of passengers."
# return columns, data, message, chart, report

import frappe


def execute(filters=None):
	columns, data = [], []

	cs_data = get_cs_data(filters)

	for d in cs_data:
		row = frappe._dict({
			"passenger_name": d.passenger_name,
			"is_verified": d.is_verified
		})
		data.append(row)

	columns = get_columns()

	chart = get_chart_data(data)

	report = get_report_summary(data)

	message = "This is a message" 

	return columns, data, None, chart, report

# def get_cs_data(filters):
# 	conditions = get_conditions(filters)
# 	data = frappe.get_all(
# 		doctype="Passenger Verification",
# 		fields = ["passenger_name","is_verified"],
# 		filters = conditions
# 	)
# 	return data

def get_cs_data(filters):
    conditions = get_conditions(filters)
    
    if "passenger_name" in conditions:
        name_value = conditions.pop("passenger_name")
        conditions["passenger_name"] = ["like", f"%{name_value}%"]

    data = frappe.get_list(
        doctype="Passenger Verification",
        fields=["passenger_name", "is_verified"],
        filters=conditions
    )
    return data



def get_conditions(filters):
	conditions = {}
	for key, value in filters.items():
		if filters.get(key):
			conditions[key]=value

	return conditions

def get_columns():
	return [
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

def get_chart_data(data):
	label = ["Is Verified", "Not Verified"]

	verification_data = {
		"Is Verified" : 0,
		"Not Verified" : 0
	}

	datasets = []

	for entry in data:
		if entry.is_verified == 1:
			verification_data["Is Verified"] += 1
		else:
			verification_data["Not Verified"] += 1

	datasets.append({
		"name":"Verified Data",
		"values": [verification_data.get("Is Verified"),verification_data.get("Not Verified")]
	})

	chart = {
		"data" : {
			"labels" : label,
			"datasets": datasets
		},
		"type" : "pie",
		"height" : 300
	}

	return chart

def get_report_summary(data):
	is_verified, not_verified = 0, 0

	for entry in data:
		if entry.is_verified == 1:
			is_verified +=1
		else:
			not_verified += 1

	return [
		{
			"value":is_verified,
			"indicator":"Red",
			"label":"Verified",
			"datatype": "Int"
		},
				{
			"value":not_verified,
			"indicator":"Blue",
			"label":"Not Verified",
			"datatype": "Int"
		},
	]
