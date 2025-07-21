# Copyright (c) 2025, Mohammed Yousuf and contributors
# For license information, please see license.txt

# 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

import frappe
from frappe.model.document import Document
from frappe.website.page_renderers.base_renderer import BaseRenderer


class RequestLifecycle(BaseRenderer):
    def can_render(self):
        # Example: only handle /custom-page path
        return frappe.request.path == "/custom-page"

    def render(self):
        html = "<h1>Hello from custom renderer!</h1>"
        return self.build_response(html)

"""
Step 1: User URL send pannadhum it Identify the Request Type whether it is an api or files or website router etc.. (Frappe decides: API ah? File ah? Web Page ah?)
Step 2: Before Routing (Pre-Processing):
			Request record pannum.
			Rate limit check panrum (too many requests na block pannum)
			Then goes to Website Router
Step 3: Path Resolver - Redirect iruka illaiya nu check pannum? Route match aagudha illaiya nu paakum? suppose irundha Renderer choose pannum illa na error kaatum
Step 4: Page Renderers (Simple Overview)

"""


"""
Frappe decides how to handle a request based on the URL.
It passes through multiple stages: Preprocessing → Redirect Check → Route Match → Renderer Picked → HTML Returned.
You can override with your own logic using a custom renderer.

Steps:
1. User browses your site (like /about, /posts, /api/products, /files/something.jpg).	
	Depending on the type of request, Frappe handles it differently:
		URL Starts With						Handled By
		/api								REST API handler
		/files, /backups, /private/files	File Download Handler
		/about, /posts, /blog/something		Website Router

2. Before the URL reaches the final destination:
	- Recorder Initialized, for request tracking.
	- Rate Limiter, to avoid abuse.
	- Then, passed to the Website Router.

3. Path Resolver:Now the request enters Path Resolver. This part decides where to send the request.
 1. Redirect Resolution
	If there is a redirect rule (set in Website Settings or hooks), it follows that.
	Example: /old-blog → redirects to /new-blog
 2. Route Resolution
	No redirect? It checks if the path matches:
	website/routing/rules (hook)
	or has_web_view enabled DocTypes
 3. Renderer Selection
	Now that we know which document or page to show, it checks:
	“Which renderer can handle this path?”
	First one to say can_render → True is selected.

4. Page Renderers: Renderer = Python class that renders the page.
	Each class must have:
		def can_render(self):
			return True or False
		def render(self):
			return self.build_response("HTML content") 

5.  Standard Page Renderers:
		Renderer			Used For
		StaticPage			Serve files (PDF, images) from /public or /www
		TemplatePage		Render .html or .md files from /www
		WebformPage			Show web forms listed in Web Form Doctype
		DocumentPage		Show a single document’s page like a blog article
		ListPage			Show list view for DocTypes (Ex: all blog posts)
		PrintPage			Render printable document (with print format)
		NotFoundPage		404 Not Found
		NotPermittedPage	403 Permission Denied
"""
