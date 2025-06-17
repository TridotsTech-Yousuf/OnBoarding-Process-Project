# Copyright (c) 2025, Mohammed Yousuf and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import random
import io
import base64
import barcode
from barcode.writer import ImageWriter
from frappe.query_builder import DocType
from frappe.query_builder.functions import Count


class PassengerVerification(Document):
    def validate(self):
        if self.is_verified:
            number = random.randint(1, 10)
            letter = random.choice(['A', 'B'])
            seat_number = f"{number}{letter}"
            self.seat_number = seat_number
        
            self.barcode = self.generate_barcode_image(self.passenger_name)
        
    def generate_barcode_image(self, code):
        buffer = io.BytesIO()
        bar = barcode.get('code128', code, writer=ImageWriter())
        bar.write(buffer)
        img_bytes = buffer.getvalue()
        base64_img = "data:image/png;base64," + base64.b64encode(img_bytes).decode()
        return base64_img


# Query Builder
@frappe.whitelist()
def get_verified_passenger_luggage():
    Boarding = DocType("Boarded Passengers")
    Passenger = DocType("Passenger Verification")
    query = (
        # Simple QB Structure
        # frappe.qb.from_(Boarding).select(Boarding.passenger_name) 

        # Including Where
        # frappe.qb.from_(Boarding).select("*").where(Boarding.passenger_name=="Rinoza Samad") 

        # Including AND , OR Conditions
        # frappe.qb.from_(Boarding).select("*").where((Boarding.passenger_name=="Rinoza Samad") | (Boarding.passenger_name=="Angelina Chistian") ) 

        # Including Functions like COUNT, SUM, etc.
        # frappe.qb.from_(Boarding).select(Count("*").as_("total_passengers"))

        frappe.qb.from_(Passenger).select("*").where(Passenger.is_verified==1) 

    )
    result = query.run(as_dict=True)

    # Including Functions like COUNT, SUM, etc.
    # total_passengers = result[0]['total_passengers'] if result else 0
    # frappe.msgprint(f"Total Passengers: {total_passengers}")

    for data in result:
        frappe.msgprint(
            data.passenger_name,
        )

    if result:
        return {"status": "success", "data": result}
    else:
        return {"status": "failed"}

