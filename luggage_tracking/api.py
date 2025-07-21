import frappe
import csv
import io
import json
from luggage_tracking.search.passenger_search import PassengerSearch
from frappe.query_builder import DocType
from frappe.query_builder.functions import Count
import random
# from frappe import csrf
from frappe import _
import google.generativeai as genai


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

# Before Migrate Hook
def before_migrate():
    print("Before Migrate Occured -----------------------------------------------------------------")

# After Migrate Hook
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

# @frappe.whitelist()
# def search_luggage(passenger_name):
#     searcher = PassengerSearch("passenger_index")
#     results = searcher.search(passenger_name)

#     print("Searcher",searcher)
#     print("Results",results)

#     luggages = []

#     if results:
#         for r in results:
#             doc = frappe.get_doc("Passenger Verification", r["name"])
#             passenger_name_value = doc.passenger_name

#             luggage_docs = frappe.get_all("Luggage", filters={"passenger_name": passenger_name_value}, fields=["name", "passenger_name"])
            
#             if luggage_docs:
#                 for l in luggage_docs:
#                     luggages.append({
#                         "passenger_name": l.passenger_name,
#                     })
#                 return {"status": "ok", "results": luggages}
#             else:
#                 return {"status": "not ok", "results": []}
#     else:
#         return {"status": "error", "results": []}

@frappe.whitelist()
def search_luggage(passenger_name):
    print(f"[DEBUG] Starting search_luggage for: {passenger_name}---------------------------------1")

    searcher = PassengerSearch("passenger_index")
    results = searcher.search(passenger_name)

    print(f"[DEBUG] Search Results: {results}-----------------------------------2")

    luggages = []

    if results:
        for r in results:
            try:
                print(f"[DEBUG] Fetching Passenger Doc: {r['name']}------------------------------3")
                doc = frappe.get_doc("Passenger Verification", r["name"])
                passenger_name_value = doc.passenger_name

                print(f"[DEBUG] Passenger Name Found: {passenger_name_value}-----------------------------------------------4")

                luggage_docs = frappe.get_all(
                    "Luggage",
                    filters={"passenger_name": passenger_name_value},
                    fields=["name", "passenger_name"]
                )

                print(f"[DEBUG] Matching Luggage Docs: {luggage_docs}---------------------------------------5")

                for l in luggage_docs:
                    luggages.append({
                        "passenger_name": l.passenger_name,
                    })

            except Exception as e:
                frappe.logger().error(f"[ERROR] Error processing passenger: {r['name']} -> {e}")

        if luggages:
            print(f"[DEBUG] Luggage Found: {luggages}-------------------------------------------------------------6")
            return {"status": "ok", "results": luggages}
        else:
            print(f"[DEBUG] No Luggage Found for: {passenger_name}---------------------------------------------------7")
            return {"status": "not ok", "results": []}
    else:
        print(f"[DEBUG] No passenger found in search for: {passenger_name}-------------------------------------------------8")
        return {"status": "error", "message": "No matching passengers found"}


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


@frappe.whitelist(allow_guest=True)
def check_lang():
    return {
        "lang": frappe.form_dict._lang,
        "Test":"True"
    }



# @frappe.whitelist()
# def chatbot_reply(prompt):
#     prompt = prompt.lower()

#     # 🧠 Step 1: Custom command - Create Passenger Verification
#     if "create passenger verification" in prompt:
#         try:
#             name = prompt.split("name")[1].split("and")[0].strip().title()
#             status = prompt.split("status")[1].strip().title()

#             doc = frappe.get_doc({
#                 "doctype": "Passenger Verification",
#                 "passenger_name": name,
#                 "status": status
#             })
#             doc.insert()
#             return f"✅ Passenger '{name}' with status '{status}' created successfully."
#         except Exception as e:
#             return f"❌ Failed to create Passenger Verification: {e}"

#     # 🧠 Step 2: If no known commands, ask Gemini
#     try:
#         api_key = frappe.conf.get("google_gemini_api_key") 
#         genai.configure(api_key=api_key)
#         model = genai.GenerativeModel('models/gemini-2.5-pro')
#         response = model.generate_content(prompt)
#         return response.text
#     except Exception as e:
#         return f"❌ AI Error: {str(e)}"

import json

@frappe.whitelist()
def chatbot_reply(prompt):
    prompt = prompt.strip()
    session = frappe.get_doc("Chatbot Session")

    # Start flow
    if session.step == "Start":
        if prompt.lower() == "create doctype":
            session.step = "Ask Doctype Name"
            session.save()
            return "📝 What should be the name of the new Doctype?"

    # Step 1: Ask Doctype name
    elif session.step == "Ask Doctype Name":
        session.doctype_name = prompt.title()
        session.step = "Ask Field Count"
        session.save()
        return f"🔢 How many fields should '{session.doctype_name}' have?"

    # Step 2: Ask number of fields
    elif session.step == "Ask Field Count":
        try:
            count = int(prompt)
            session.field_count = count
            session.current_field_index = 0
            session.fields_info = json.dumps([])  # Init empty list
            session.step = "Ask Field Name"
            session.save()
            return f"✍️ Enter name of field 1:"
        except:
            return "❌ Please enter a valid number."

    # Step 3: Ask field details (name, type)
    elif session.step == "Ask Field Name":
        fields = json.loads(session.fields_info)
        fields.append({"fieldname": prompt})
        session.fields_info = json.dumps(fields)
        session.step = "Ask Field Type"
        session.save()
        return f"🔧 What type should field '{prompt}' be? (e.g., Data, Int, Date, Select)"

    elif session.step == "Ask Field Type":
        fields = json.loads(session.fields_info)

        # Map common user-friendly terms to real Frappe fieldtypes
        input_type = prompt.strip().lower()
        fieldtype_map = {
            "data": "Data",
            "int": "Int",
            "integer": "Int",
            "date": "Date",
            "select": "Select",
            "dropdown": "Select",
            "text": "Text",
            "small text": "Text",
            "long text": "Text",
            "check": "Check",
            "checkbox": "Check"
        }

        # Match cleaned user input
        if input_type not in fieldtype_map:
            return f"❌ '{prompt}' is not a valid field type. Try one of: {', '.join(fieldtype_map.keys())}"

        valid_fieldtype = fieldtype_map[input_type]
        fields[-1]["fieldtype"] = valid_fieldtype
        session.fields_info = json.dumps(fields)
        session.current_field_index += 1

        if session.current_field_index < session.field_count:
            session.step = "Ask Field Name"
            session.save()
            return f"✍️ Enter name of field {session.current_field_index + 1}:"
        else:
            session.step = "Creating Doctype"
            session.save()
            return create_custom_doctype_from_session(session)



    return "🤖 Sorry, something went wrong. Resetting..."

def create_custom_doctype_from_session(session):
    try:
        fields = json.loads(session.fields_info)
        doc = frappe.new_doc("DocType")
        doc.name = session.doctype_name
        doc.module = "Custom"  # or your app's module
        doc.custom = 1

        # Append fields correctly
        RESERVED_FIELDNAMES = ["name", "owner", "creation", "modified", "modified_by", "docstatus", "idx"]

        for f in fields:
            fieldname = f["fieldname"].lower().replace(" ", "_")
            
            # Avoid reserved fieldnames
            if fieldname in RESERVED_FIELDNAMES:
                fieldname = f"custom_{fieldname}"

            doc.append("fields", {
                "fieldname": fieldname,
                "label": f["fieldname"],
                "fieldtype": f["fieldtype"]
            })


        # Add basic permission
        doc.append("permissions", {
            "role": "System Manager",
            "read": 1,
            "write": 1,
            "create": 1,
            "delete": 1
        })

        doc.save()  # use save() instead of insert() for custom Doctype

        # Reset session
        session.step = "Start"
        session.doctype_name = ""
        session.field_count = 0
        session.current_field_index = 0
        session.fields_info = ""
        session.save()

        return f"✅ Custom Doctype '{doc.name}' created with {len(fields)} fields!"
    except Exception as e:
        return f"❌ Error while creating Doctype: {e}"
