# Copyright (c) 2025, Mohammed Yousuf and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _


class LanguageResolution(Document):
	def validate(self):
		lang = frappe.form_dict._lang
		print(lang,"------------------------------------------")


"""
The language for your session depends on the value of frappe.lang. Frappe decides which language to use in this priority order. 

1. Form Dict > _lang (Highest Priority):
	- If URL-la like ?_lang=ta nu kudutha, adha first priority. Temporary for that request (e.g., print view or email templates).
	- Setting this will update all translatable components in given request. 

2. Cookie > preferred\_language _[Guest User only, Ignored for logged in users]_:
	Browser cookie-la set pannirundha value. Website users (not logged in) ku useful.
	If you want persistent yet temporary language setting, you can set the preferred_language key in cookies. 

3. Request Header > Accept-Language _[Guest User only, Ignored for logged in users]_:
	Browser sends preferred languages (e.g., en-US, fr). Frappe picks the best match.

4. User document > language:
	Logged-in user's language setting (User.language field).Works across devices — persistent.

5. System Settings > language (Low Priority):
	Whole site default language. Last fallback if nothing else is set.
"""