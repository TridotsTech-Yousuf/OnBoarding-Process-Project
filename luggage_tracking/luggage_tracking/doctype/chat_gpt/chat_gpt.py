# # Copyright (c) 2025, Mohammed Yousuf and contributors
# # For license information, please see license.txt

# # Google Gemini AI API Key: AIzaSyAXlCbVzgrnZabxc2fFDiOS5Hlk36UJB9w

# import frappe
# from frappe.model.document import Document
# import google.generativeai as genai

# class ChatGPT(Document):
#     def before_save(self):
#         # self.answer = get_gemini_response(self.prompt)  
#         self.answer = get_response_with_retry(self.prompt)  



# def get_gemini_response(prompt):
#     api_key = frappe.conf.get("google_gemini_api_key")
#     genai.configure(api_key=api_key)

#     # Code to check list of models available in gemini ais
#     # models = genai.list_models()
#     # for model in models:
#     #     print(model.name,"--------")

#     try:
#         model = genai.GenerativeModel(model_name="models/gemini-2.5-pro")
#         response = model.generate_content(prompt)
#         return response.text 

#     except Exception as e:
#         frappe.throw(f"Gemini Error: {e}")

# # In chat_gpt.py
# @frappe.whitelist()
# def chat_with_gpt(prompt):
#     return get_response_with_retry(prompt)

# def get_response_with_retry(prompt):
#     if "create todo" in prompt.lower():
#         task = frappe.get_doc({
#             "doctype": "ToDo",
#             "subject": prompt.replace("create todo", "").strip(),
#             "status": "Open"
#         }).insert()
#         return f"✅ Task '{task.subject}' created."

#     elif "sales today" in prompt.lower():
#         from frappe.utils import nowdate
#         total = frappe.db.sql("""
#             SELECT SUM(grand_total) FROM `tabSales Invoice`
#             WHERE posting_date = %s AND docstatus = 1
#         """, (nowdate(),))[0][0]
#         return f"📊 Today's Sales: ₹{total or 0}"

#     # Fallback to Gemini
#     return get_gemini_response(prompt)

# Copyright (c) 2025, Mohammed Yousuf and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document
# import google.generativeai as genai

# class ChatGPT(Document):
#     def before_save(self):
#         self.answer = get_response_with_retry(self.prompt)

# @frappe.whitelist()
# def chat_with_gpt(prompt):
#     return get_response_with_retry(prompt)

# def get_response_with_retry(prompt):
#     prompt_lower = prompt.lower()

#     if "create todo" in prompt_lower or "add todo" in prompt_lower:
#         description = prompt.replace("create todo", "").replace("add todo", "").strip()
#         todo = frappe.get_doc({
#             "doctype": "ToDo",
#             "description": description,
#             "allocated_to": frappe.session.user,
#             "status": "Open"
#         }).insert()
#         return f"📝 ToDo '{description}' created for {frappe.session.user}."

#     elif "sales today" in prompt_lower:
#         from frappe.utils import nowdate
#         total = frappe.db.sql("""
#             SELECT SUM(grand_total) FROM `tabSales Invoice`
#             WHERE posting_date = %s AND docstatus = 1
#         """, (nowdate(),))[0][0]
#         return f"📊 Today's Sales: ₹{total or 0}"

#     # fallback to Gemini
#     return get_gemini_response(prompt)

# def get_gemini_response(prompt):
#     api_key = frappe.conf.get("google_gemini_api_key")
#     genai.configure(api_key=api_key)

#     try:
#         model = genai.GenerativeModel(model_name="models/gemini-2.5-pro")
#         response = model.generate_content(prompt)
#         return response.text
#     except Exception as e:
#         frappe.throw(f"Gemini Error: {e}")

import frappe
from frappe.model.document import Document
import google.generativeai as genai
import json

class ChatGPT(Document):
    def before_save(self):
        self.answer = get_response_with_retry(self.prompt)

@frappe.whitelist()
def chat_with_gpt(prompt):
    return get_response_with_retry(prompt)

def get_response_with_retry(prompt):
    prompt_lower = prompt.lower()

    if "create todo" in prompt_lower or "add todo" in prompt_lower:
        description = prompt.replace("create todo", "").replace("add todo", "").strip()
        todo = frappe.get_doc({
            "doctype": "ToDo",
            "description": description,
            "allocated_to": frappe.session.user,
            "status": "Open"
        }).insert()
        return f"📝 ToDo '{description}' created for {frappe.session.user}."

    elif "sales today" in prompt_lower:
        from frappe.utils import nowdate
        total = frappe.db.sql("""
            SELECT SUM(grand_total) FROM `tabSales Invoice`
            WHERE posting_date = %s AND docstatus = 1
        """, (nowdate(),))[0][0]
        return f"📊 Today's Sales: ₹{total or 0}"

    elif "create doctype" in prompt_lower:
        return create_doctype_from_prompt(prompt)

    # fallback to Gemini
    return get_gemini_response(prompt)

def get_gemini_response(prompt):
    api_key = frappe.conf.get("google_gemini_api_key")
    genai.configure(api_key=api_key)

    try:
        model = genai.GenerativeModel(model_name="models/gemini-2.5-pro")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        frappe.throw(f"Gemini Error: {e}")

# 🔧 Create Doctype Logic
def create_doctype_from_prompt(prompt):
    """
    Sample prompt: create doctype ContactForm with fields name (Data), phone (Phone), email (Email)
    """
    api_key = frappe.conf.get("google_gemini_api_key")
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("models/gemini-2.5-pro")
    system_prompt = """
    You are an expert in ERPNext and Frappe framework. 
    When the user gives a prompt like "create doctype <name> with fields name (Data), age (Int)", 
    you must convert it into a JSON like:
    {
      "name": "ContactForm",
      "fields": [
        {"label": "Name", "fieldname": "name", "fieldtype": "Data"},
        {"label": "Phone", "fieldname": "phone", "fieldtype": "Phone"},
        {"label": "Email", "fieldname": "email", "fieldtype": "Email"}
      ]
    }
    Only return the JSON.
    """

    result = model.generate_content(prompt)

    try:
        doc_info = json.loads(result.text)
        doctype_name = doc_info["name"]
        fields_info = doc_info["fields"]

        doc = frappe.new_doc("DocType")
        doc.name = doctype_name
        doc.module = "Custom"
        doc.custom = 1
        doc.is_submittable = 0
        doc.is_tree = 0

        for f in fields_info:
            doc.append("fields", {
                "label": f["label"],
                "fieldname": f["fieldname"].lower().replace(" ", "_"),
                "fieldtype": f["fieldtype"]
            })

        doc.insert()
        return f"✅ Doctype '{doctype_name}' created with {len(fields_info)} fields."

    except Exception as e:
        return f"❌ Failed to create Doctype: {e}\nGemini Response: {result.text}"
