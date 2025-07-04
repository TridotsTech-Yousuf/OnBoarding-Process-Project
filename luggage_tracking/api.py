import frappe
import csv
import io
import json
from luggage_tracking.search.passenger_search import PassengerSearch
from frappe.query_builder import DocType
from frappe.query_builder.functions import Count
import random
# from frappe import csrf


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

def default_homepage(user):
    user_roles = frappe.get_roles(user)
    if "System Manager" in user_roles:
        # print("System Manager -------------------------------------------------------------")
        return "admin"
    elif "Sales Manager" in user_roles:
        # print("Sales Manager -------------------------------------------------------------")
        return "salesManager"
    elif "Accounts Manager" in user_roles:
        # print("Accounts Manager -------------------------------------------------------------")
        return "accountsManager"
    else:
        return "index"
    
def braintree_success_page(data):
    print(data.reference_doctype, "-----------------------------------------")
    print(data.reference_docname,"----------------------------------------------")
    return "thank-you"


@frappe.whitelist()
def get_passenger_luggage():
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

        # frappe.qb.from_(Passenger).select("*").where(Passenger.is_verified==1) 

        frappe.qb.from_(Passenger).select("*")
    )
    result = query.run(as_dict=True)

    if result:
        return {"status": "success", "data": result}
    else:
        return {"status": "failed"}

@frappe.whitelist()
def get_verified_passenger_luggage():
    Passenger = DocType("Passenger Verification")

    verified_passengers_list = (
        frappe.qb.from_(Passenger)
        .select("*")
        .where(Passenger.is_verified == 1)
    )

    count_of_list = (
        frappe.qb.from_(Passenger)
        .select(Count("*").as_("total_verified_passengers"))
        .where(Passenger.is_verified == 1)
    )

    result = verified_passengers_list.run(as_dict=True)
    count_result = count_of_list.run(as_dict=True)

    if result:
        return {
            "status": "success",
            "data": result,
            "count": count_result[0]["total_verified_passengers"]
        }
    else:
        return {
            "status": "failed",
            "message": "No verified passengers found"
        }



@frappe.whitelist()
def get_luggage_details():
    print("Query Builder Fetch Started -----------------------------")

    # Define tables
    Passenger = DocType("Passenger Verification")
    Luggage = DocType("Luggage")
    LuggageDetails = frappe.qb.Table("tabLuggage Details")

    # Query with JOIN on child table via `parent`
    query = (
        frappe.qb
        .from_(Passenger)
        .join(Luggage)
        .on(Passenger.passenger_name == Luggage.passenger_name)
        .join(LuggageDetails)
        .on(Luggage.name == LuggageDetails.parent)
        .select("*")
    )

    result = query.run(as_dict=True)
    # print(result, "-------------------- All Luggage with Child Details --------------------------")

    if result:
        return {
            "status": "success",
            "data": result,
            "count": len(result)
        }
    else:
        return {
            "status": "failed",
            "message": "No verified luggage data found"
        }


