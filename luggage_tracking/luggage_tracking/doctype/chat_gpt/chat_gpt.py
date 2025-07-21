# Copyright (c) 2025, Mohammed Yousuf and contributors
# For license information, please see license.txt

# Google Gemini AI API Key: AIzaSyAXlCbVzgrnZabxc2fFDiOS5Hlk36UJB9w

import frappe
from frappe.model.document import Document
import google.generativeai as genai

class ChatGPT(Document):
    def before_save(self):
        self.answer = get_gemini_response(self.prompt)  


def get_gemini_response(prompt):
    api_key = frappe.conf.get("google_gemini_api_key")
    genai.configure(api_key=api_key)

    # Code to check list of models available in gemini ais
    # models = genai.list_models()
    # for model in models:
    #     print(model.name,"--------")

    try:
        model = genai.GenerativeModel(model_name="models/gemini-2.5-pro")
        response = model.generate_content(prompt)
        return response.text 

    except Exception as e:
        frappe.throw(f"Gemini Error: {e}")

