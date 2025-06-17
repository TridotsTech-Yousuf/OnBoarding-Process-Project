# Copyright (c) 2025, Mohammed Yousuf and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import now_datetime


class LuggageStatusUpdate(Document):
	pass

@frappe.whitelist()
def update_luggage_status_from_scan(check_in_luggage_id):
	if not check_in_luggage_id:
		return "No Luggage ID provided"


	luggage_list = frappe.get_all("Luggage", filters={"check_in_luggage_id": check_in_luggage_id}, fields=["name"])
	if not luggage_list:
		return "Luggage not found"

	luggage = frappe.get_doc("Luggage", luggage_list[0].name)
	statuses = ["Checked-in", "Loaded", "In Transit", "Unloaded", "In Claim Area", "Collected"]

	if luggage.tracking and luggage.tracking[-1].status:
		current_status = luggage.tracking[-1].status
	else:
		current_status = "Checked-in"

	try:
		current_index = statuses.index(current_status)
		next_status = statuses[current_index + 1]
	except (ValueError, IndexError):
		return f"Cannot update status from '{current_status}'"

	if next_status == "Loaded":
		passenger_doc = frappe.get_all(
			"Passenger Verification",
			filters={"passenger_name": luggage.passenger_name},
			fields=["name", "departure_airport"],
			limit=1
		)
		if not passenger_doc:
			return f"Passenger Verification for {luggage.passenger_name} not found"
		location = passenger_doc[0].departure_airport

	elif next_status in ["Unloaded", "In Claim Area", "Collected"]:
		passenger_doc = frappe.get_all(
			"Passenger Verification",
			filters={"passenger_name": luggage.passenger_name},
			fields=["name", "arrival_airport"],
			limit=1
		)
		if not passenger_doc:
			return f"Passenger Verification for {luggage.passenger_name} not found"
		location = passenger_doc[0].arrival_airport

	elif next_status == "In Transit":
		location = "In Airplane"

	luggage.append("tracking", {
        "status": next_status,
        "time_stamp": now_datetime(),
        "location": location
    })

	luggage.status = next_status
	luggage.save()

	return f"Status updated to {next_status}"

