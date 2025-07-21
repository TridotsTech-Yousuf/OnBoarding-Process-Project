# Copyright (c) 2025, Mohammed Yousuf and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import io
import base64
import barcode
from barcode.writer import ImageWriter
import random

class Luggage(Document):
    def autoname(self):
        self.create_check_in_luggage_id()

    def validate(self):
        total_weight = 0
        check_in_luggage_weight = 0
        cabin_luggage_weight = 0

        for item in self.luggage_details:
            total_weight += item.weight
            if item.luggage_type == "Check IN":
                check_in_luggage_weight += item.weight
            elif item.luggage_type == "Cabin":
                cabin_luggage_weight += item.weight

        self.total_weight = total_weight

        # ✅ Skip validation if payment is already made
        if self.payment_id:
            # Allow any weight without validation
            self.additional_check_in_luggage_weight = max(0, check_in_luggage_weight - 25)
            self.additional_cabin_luggage_weight = max(0, cabin_luggage_weight - 7)
            return

        # 🚫 Apply validation if payment not made
        self.additional_check_in_luggage_weight = 0
        if check_in_luggage_weight < 0:
            frappe.throw("Check In Luggage cannot be negative.")
        elif check_in_luggage_weight > 25:
            frappe.throw("Check In Luggage cannot exceed 25kg.")

        self.additional_cabin_luggage_weight = 0
        if cabin_luggage_weight < 0:
            frappe.throw("Cabin Luggage cannot be negative.")
        elif cabin_luggage_weight > 7:
            frappe.throw("Cabin Luggage cannot exceed 7kg.")

        
    # def validate(self):
    #     total_weight = 0
    #     check_in_luggage_weight = 0 
    #     cabin_luggage_weight = 0

    #     for item in self.luggage_details:
    #         total_weight += item.weight
    #         if item.luggage_type == "Check IN":
    #             check_in_luggage_weight += item.weight
    #         elif item.luggage_type == "Cabin":
    #             cabin_luggage_weight += item.weight
    #     self.total_weight = total_weight

    # def autoname(self):
    #     pass
        
    # def check_in_luggage_validation(self, check_in_luggage_weight):
    #     self.additional_check_in_luggage_weight = 0

    #     if check_in_luggage_weight:
    #         if check_in_luggage_weight <= 25:
    #             if check_in_luggage_weight > 0:
    #                 pass
    #             else:
    #                 frappe.throw("Check In Luggage Cannot be a Negative value.")
    #         else:
    #             self.additional_check_in_luggage_weight = check_in_luggage_weight-25
    #             frappe.throw(f"Check-in luggage should be under 25kg. Additional luggage weight: {self.additional_check_in_luggage_weight}kg.")

    # def cabin_luggage_validation(self, cabin_luggage_weight):
    #     self.additional_cabin_luggage_weight = 0

    #     if cabin_luggage_weight:
    #         if cabin_luggage_weight <= 7:
    #             if cabin_luggage_weight > 0:
    #                 pass
    #             else:
    #                 frappe.throw("Cabin Luggage Cannot be a Negative value.")
    #         else:
    #             self.additional_cabin_luggage_weight = cabin_luggage_weight-7
    #             frappe.throw(f"Cabin luggage should be under 7kg. Additional luggage weight: {self.additional_cabin_luggage_weight}kg.")


    def before_save(self):
        if self.tracking:
            for data in self.tracking:
                if data.status and not data.time_stamp:
                    data.time_stamp = frappe.utils.now_datetime()
                    if data.status == "Loaded":
                        data.location = frappe.get_value("Passenger Verification", {"passenger_name": self.passenger_name}, "departure_airport")
                    elif data.status == "Unloaded" or data.status == "In Claim Area" or data.status == "Collected":
                        data.location = frappe.get_value("Passenger Verification", {"passenger_name": self.passenger_name}, "arrival_airport")
                    elif data.status == "In Transit":
                        data.location = "In Airplane"
							
        if self.tracking:
            last_row = self.tracking[-1]
            if last_row.status:
                self.status = last_row.status
                self.last_updated = last_row.time_stamp
            else:
                last_row.status = "Checked-in"
        else:
            self.status = "Checked-in"
            self.append("tracking", {
				"status": self.status,
				"time_stamp": frappe.utils.now_datetime(),
				"location": frappe.get_value("Passenger Verification", {"passenger_name": self.passenger_name}, "departure_airport")
			})
            self.last_updated = frappe.utils.now_datetime()

        self.barcode = self.generate_barcode_image(self.check_in_luggage_id)

		
    def create_check_in_luggage_id(self):
        if not self.check_in_luggage_id:
            random_part = str(random.randint(11, 99))
            self.check_in_luggage_id = f"CHKN{random_part}"

    def generate_barcode_image(self, code):
        buffer = io.BytesIO()
        bar = barcode.get('code128', code, writer=ImageWriter())
        bar.write(buffer)
        img_bytes = buffer.getvalue()
        base64_img = "data:image/png;base64," + base64.b64encode(img_bytes).decode()
        return base64_img


# Eample for Request Life Cycle
@frappe.whitelist()
def download_luggage_tag(passenger_name):
    if passenger_name:
        frappe.msgprint("Passenger Name")

        pdf_content = f"Luggage Tag for Passenger: {passenger_name}".encode()

        frappe.response["filename"] = f"luggage_tag_{passenger_name}.txt"
        frappe.response["filecontent"] = pdf_content
        frappe.response["type"] = "download"
        frappe.response["display_content_as"] = "attachment"

    else:
        frappe.msgprint("No Passenger Name")

# @frappe.whitelist()
