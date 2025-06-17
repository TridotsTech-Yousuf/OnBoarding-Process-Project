# Copyright (c) 2025, Mohammed Yousuf and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns, data = [], []

	cs_data = get_cs_data(filters)

	for d in cs_data:
		row = frappe._dict({
			"passenger_name": d.passenger_name,
			"status":d.status
		})
		data.append(row)
	
	columns = get_columns()

	chart = get_chart_data(data)

	report = get_report_summary(data)

	return columns, data, None, chart, report



def get_cs_data(filters):
	conditions = get_conditions(filters)
	data = frappe.get_all(
		doctype="Luggage",
		fields = ["passenger_name","status"],
		filters = conditions
	)
	return data

def get_conditions(filters):
	conditions = {}
	for key, value in filters.items():
		if filters.get(key):
			conditions[key]=value

	return 

def get_columns():
	return [
		{
			"fieldname":"passenger_name",
			"label": "Passenger Name",
			"fieldtype": "Data",
		},
		{
			"fieldname":"status",
			"label": "Current Status",
			"fieldtype": "Select",
		}
	]

def get_chart_data(data):
	label = ["Checked-in","Loaded", "In Transit", "Unloaded", "In Claim Area", "Collected"]

	verification_data = {
		"Checked-in":0,
		"Loaded" : 0,
		"In Transit" : 0,
		"Unloaded" :0,
		"In Claim Area" :0,
		"Collected":0
	}

	datasets = []

	for entry in data:
		if entry.status == "Checked-in":
			verification_data["Checked-in"] += 1
		elif entry.status == "Loaded":
			verification_data["Loaded"] += 1
		elif entry.status == "In Transit":
			verification_data["In Transit"] +=1
		elif entry.status == "Unloaded":
			verification_data["Unloaded"] +=1
		elif entry.status == "In Claim Area":
			verification_data["In Claim Area"] +=1
		elif entry.status == "Collected":
			verification_data["Collected"] += 1

	datasets.append({
		"name":"Luggage Status",
		"values": [verification_data.get("Checked-in"),verification_data.get("Loaded"),verification_data.get("In Transit"), verification_data.get("Unloaded"), verification_data.get("In Claim Area"), verification_data.get("Collected")]
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
	checkedIN, loaded, inTransit, unloaded, inClaimArea, collected = 0, 0, 0, 0, 0, 0

	for entry in data:
		if entry.status == "Checked-in":
			checkedIN += 1
		elif entry.status == "Loaded":
			loaded += 1
		elif entry.status == "In Transit":
			inTransit +=1
		elif entry.status == "Unloaded":
			unloaded +=1
		elif entry.status == "In Claim Area":
			inClaimArea +=1
		elif entry.status == "Collected":
			collected += 1

	return [
		{
			"value":checkedIN,
			"indicator":"Orange",
			"label":"Checked IN",
			"datatype": "Int"
		},
		{
			"value":loaded,
			"indicator":"Red",
			"label":"Loaded",
			"datatype": "Int"
		},
		{
			"value":inTransit,
			"indicator":"Blue",
			"label":"In Transit",
			"datatype": "Int"
		},
		{
			"value":unloaded,
			"indicator":"Green",
			"label":"Un Loaded",
			"datatype": "Int"
		},
				{
			"value":inClaimArea,
			"indicator":"Yellow",
			"label":"In Claim Area",
			"datatype": "Int"
		},
				{
			"value":collected,
			"indicator":"Pink",
			"label":"Collected",
			"datatype": "Int"
		},
	]
