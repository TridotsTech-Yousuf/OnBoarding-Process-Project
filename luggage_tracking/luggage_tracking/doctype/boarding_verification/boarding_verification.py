import frappe
from frappe.model.document import Document

class BoardingVerification(Document):
	pass

@frappe.whitelist()
def fetch_boarding_verification_data(passenger_name):
	if passenger_name:
		passenger = frappe.db.get_all(
			"Passenger Verification",
			filters={"passenger_name": passenger_name},
			fields=["seat_number","is_verified", "e_ticket_number", "status", "class_of_service"]
		)

		if passenger:
			
			return {
				"seat_number": passenger[0].get("seat_number"),
				"is_verified": passenger[0].get("is_verified"),
				"e_ticket_number": passenger[0].get("e_ticket_number"),
				"status" : passenger[0].get("status"),
				"class_of_service": passenger[0].get("class_of_service"),
				"boarded":1
			}
		else:
			frappe.throw(f"Passenger Verification not found for {passenger_name}")
	else:
		frappe.throw("Passenger Name is required")

@frappe.whitelist()
def create_boarded_passenger(data):
    import json
    data = json.loads(data)

    # Check if record already exists
    existing = frappe.db.exists(
        "Boarded Passengers",
        {
            "passenger_name": data.get("passenger_name"),
            "seat_number": data.get("seat_number")
        }
    )
    if existing:
        return existing

    doc = frappe.new_doc("Boarded Passengers")
    doc.passenger_name = data.get("passenger_name")
    doc.seat_number = data.get("seat_number")
    doc.is_verified = data.get("is_verified")
    doc.e_ticket_number = data.get("e_ticket_number")
    doc.status = data.get("status")
    doc.class_of_service = data.get("class_of_service")
    doc.boarded = data.get("boarded")
    doc.insert()
    frappe.db.commit()
    return doc.name