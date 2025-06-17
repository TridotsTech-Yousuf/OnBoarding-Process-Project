import frappe
import csv
import io
import json
from luggage_tracking.search.passenger_search import PassengerSearch

def export_passenger_data():
    # Get the data
    passengers = frappe.db.get_all('Boarded Passengers', fields=["name", "passenger_name"])

    # Create a CSV in memory
    output = io.StringIO()
    writer = csv.writer(output)

    # Write headers
    writer.writerow(["Name", "Passenger Name"])

    # Write data rows
    for p in passengers:
        writer.writerow([p.name, p.passenger_name])

    # Create the file in Frappe
    csv_content = output.getvalue()
    file_name = "Boarded_Passengers_Export.csv"

    # Save file to File doctype
    frappe.get_doc({
        "doctype": "File",
        "file_name": file_name,
        "is_private": 0,
        "content": csv_content
    }).insert(ignore_permissions=True)

    # Delete all Boarded Passengers records
    for p in passengers:
        frappe.delete_doc('Boarded Passengers', p.name, ignore_permissions=True)

    # Commit the changes to make sure all deletions are saved
    frappe.db.commit()

    # Optional log
    frappe.log_error("Exported Passenger List", json.dumps(passengers, indent=2))

def before_migrate():
    print("Before Migrate Occured -----------------------------------------------------------------")

def after_migrate():
    print("After Migrate Occured ------------------------------------------------------------")

def boot_session(bootinfo):
    bootinfo.my_global_key = "my_global_value"
    
def custom_website_context(context):
    context.my_key = "my_value"

def get_context(context):
    context.custom_message = "This is a dummy extension!"
    frappe.log_error("Get Context Called")
    return context

def clear_website_cache(path=None):
    if path:
        print("Path cache cleared")
    else:
        print("All cache cleared")

# def resolve_path(path):
#     if path == "dummy-resolve":
#         return {
#             "path": "hello"
#         }


#     # Log if unknown
#     frappe.logger().info(f"resolve_path hook called for: {path}")
#     return None

@frappe.whitelist()
def search_luggage(passenger_name):
    searcher = PassengerSearch("passenger_index")
    results = searcher.search(passenger_name)

    luggages = []

    if results:
        for r in results:
            doc = frappe.get_doc("Passenger Verification", r["name"])
            passenger_name_value = doc.passenger_name

            luggage_docs = frappe.get_all("Luggage", filters={"passenger_name": passenger_name_value}, fields=["name", "passenger_name"])
            
            if luggage_docs:
                for l in luggage_docs:
                    luggages.append({
                        "passenger_name": l.passenger_name,
                    })
                return {"status": "ok", "results": luggages}
            else:
                return {"status": "not ok", "results": []}

    else:
        frappe.msgprint(f"Error while searching luggage", "Luggage Search Error")

