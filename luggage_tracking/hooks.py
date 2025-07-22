app_name = "luggage_tracking"
app_title = "Luggage Tracking"
app_publisher = "Mohammed Yousuf"
app_description = "Luggage Tracking System"
app_email = "mohammedyousuf@gmail.com"
app_license = "mit"

# Apps
# ------------------


# used when your app depends on other apps to work. For example, 
# if luggage_tracking needs another app like erpnext, you would write required_apps = ["erpnext"].
# required_apps = []
 
# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "luggage_tracking",
# 		"logo": "/assets/luggage_tracking/logo.png",
# 		"title": "Luggage Tracking",
# 		"route": "/luggage_tracking",
# 		"has_permission": "luggage_tracking.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/luggage_tracking/css/luggage_tracking.css"
# app_include_js = "/assets/luggage_tracking/js/luggage_tracking.js"

# include js, css files in header of web template
# web_include_css = "/assets/luggage_tracking/css/luggage_tracking.css"
# web_include_js = "/assets/luggage_tracking/js/luggage_tracking.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "luggage_tracking/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}



# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "luggage_tracking/public/icons.svg"


# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "luggage_tracking.utils.jinja_methods",
# 	"filters": "luggage_tracking.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "luggage_tracking.install.before_install"
# after_install = "luggage_tracking.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "luggage_tracking.uninstall.before_uninstall"
# after_uninstall = "luggage_tracking.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "luggage_tracking.utils.before_app_install"
# after_app_install = "luggage_tracking.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "luggage_tracking.utils.before_app_uninstall"
# after_app_uninstall = "luggage_tracking.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "luggage_tracking.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"luggage_tracking.tasks.all"
# 	],
# 	"daily": [
# 		"luggage_tracking.tasks.daily"
# 	],
# 	"hourly": [
# 		"luggage_tracking.tasks.hourly"
# 	],
# 	"weekly": [
# 		"luggage_tracking.tasks.weekly"
# 	],
# 	"monthly": [
# 		"luggage_tracking.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "luggage_tracking.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "luggage_tracking.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "luggage_tracking.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["luggage_tracking.utils.before_request"]
# after_request = ["luggage_tracking.utils.after_request"]

# Job Events
# ----------
# before_job = ["luggage_tracking.utils.before_job"]
# after_job = ["luggage_tracking.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"luggage_tracking.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# ==========================================================================

# test_string = "value"
# test_list = ["value"]
# test_dict = {
#     "key": "value"
# }

# # Desk
# app_include_js = [
    # "https://checkout.razorpay.com/v1/checkout.js"
# ]

page_renderer = "luggage_tracking.luggage_tracking.doctype.request_lifecycle.request_lifecycle.RequestLifecycle"

# app_include_js = "/assets/luggage_tracking/js/chatbot.js"

app_include_js = "/assets/luggage_tracking/js/floating_chatbot.js"

# app_include_js = [
#     "https://checkout.razorpay.com/v1/checkout.js",
#     "/assets/luggage_tracking/js/chatbot.js",
#     "/assets/luggage_tracking/js/floating_chatbot.js"
# ]





# app_include_js = "/assets/luggage_tracking/js/app_include.js" 

# Portal 
# web_include_js = "/assets/luggage_tracking/js/web_include.js" 

# Web Form
# webform_include_js = { "Passenger Verification": "public/js/webform_include.js"} 

# Page
# page_js = {"test": "public/js/pageJs.js"} 

# Sounds - frappe.utils.play_sound("ping")
sounds = [
    {"name": "ping", "src": "/assets/luggage_tracking/sound/ping.mp3", "volume": 0.5}
]

# Install Hooks - Not Working # -----------------------------------------------------------------------
# Uninstall Hooks - Not Working # -----------------------------------------------------------------------

# Migrate Hooks
# before_migrate = "luggage_tracking.api.before_migrate"
# after_migrate = "luggage_tracking.api.after_migrate"

# Test Hooks
# before_tests = "luggage_tracking.api.before_test"

# File Hooks - Not Working # -----------------------------------------------------------------------
# Email Hooks - Not Working # -----------------------------------------------------------------------

# Extend Boot Info - console.log(frappe.boot.my_global_key)
# extend_bootinfo = "luggage_tracking.api.boot_session"

# Website Context 
# Working
# website_context = {
    # "favicon": "/assets/luggage_tracking/image/icon.png"
# }
# Not Working
# update_website_context = "luggage_tracking.api.custom_website_context"

# Website Controller Context - Page Changing but data not passing from python to html
# extend_website_page_controller_context = {
    # "frappe.www.404": "luggage_tracking.api.get_context"
# }

# Web pages with dynamic routes - Not Working # ---------------------------------------------------

# Website Clear Cache - bench clear-website-cache
# website_clear_cache = "luggage_tracking.api.clear_website_cache"

# Website Redirects 
# website_redirects = [
#     {"source": "/hello", "target": "/about"},
# ]

# Website Route Rules
# website_route_rules = [
#     {"from_route": "/serma", "to_route": "/hello"},
# ]

# Website Path Resolver - Not Working # ----------------------------------------------------------
# website_path_resolver = "inventory_management.utils.custom_path_resolver"


# Website 404 - Not Working # --------------------------------------------------------------------

# Default Homepage
# homepage = "homepage"
# Default Homepage - Role based homepage 
# role_home_page = {
#     "Accounts Manager": "accountsManager",
#     "Sales Manager": "salesManager"
# }
# Default Homepage - More control over the logic 
# get_website_user_home_page = "luggage_tracking.api.default_homepage"

# Portal Side Bar
# portal_menu_items = [
#     {"title": "Account", "route": "/accountsManager", "role": "Accounts Manager"},
#     {"title": "Sales", "route": "/salesManager", "role": "Accounts Manager"},
# ]
# synced with the database. Not Working ----------------------------------------------------
# standard_portal_menu_items = [
#     {"title": "Account", "route": "/accountsManager", "role": "Accounts Manager"},
#     {"title": "Sales", "route": "/salesManager", "role": "Accouts Manager"},
# ]

# Brand HTML - Image Not Coming --------------------------------
# brand_html = '<div> <img src="/assets/luggage_tracking/image/y.jpg" style="height: 60px;"> Yousuf</div>'

# Base Template 
# base_template = "luggage_tracking/templates/my_custom_base.html"

# Not working -----------------------------------------------------------------------------
# base_template_map = {
#     r"docs.*": "app/templates/doc_template.html"
# }

# Not working -----------------------------------------------------------------------------
# Integrations - Braintree Success Page 
# braintree_success_page = "luggage_tracking.api.braintree_success_page"

# Calenders - Doctype 
# calendars = ["Passenger Verification"]

# Clear Cache
# clear_cache = "luggage_tracking.cache.clear_cache"

# Default Mail Footer 
# default_mail_footer = """
#  <div>
#  Sent via <a href="https://youtube.com" target="_blank">Youtube</a>
# </div>
# """

# Session Hook
# on_login = "luggage_tracking.utils.successful_login"
# on_session_creation = "luggage_tracking.utils.allocate_free_credits"
# on_logout = "luggage_tracking.utils.clear_user_cache"

# Auth Hook
# auth_hooks = ["app.overrides.validate_custom_jwt"]

# Fixtures
# fixtures = [
#     # export all records from the Category table
#     "Passenger Verification"
# ]


scheduler_events = {
    "Cron": {
        "0 0 * * *": [
            "luggage_tracking.api.export_passenger_data"
        ] 
    } 
} 

# -------------------------------------------------------------

# before_install = "luggage_tracking.install.before_install"
# before_install = "app.setup.install.before_install"
# before_install = "luggage_tracking.api.before_install"
# adter_install = "luggage_tracking.api.after_install"

# before_write_file = "luggage_tracking.api.before_write"
# write_file = "luggage_tracking.api.write_file"
# delete_file_data_content = "luggage_tracking.api.delete_file"


# get_web_pages_with_dynamic_routes = "script.get_web_pages_with_dynamic_routes"




# website_path_resolver = "luggage_tracking.api.resolve_path"











# website_catch_all = "not_found"







# override_email_send = "app.overrides.email.send"
# get_sender_details = "app.overrides.email.get_sender_details"




# app_include_icons = "luggage_tracking/public/icon.png"

# doctype_js = {"doctype" : "public/js/doctypeJs.js"} 
# doctype_list_js = {"doctype" : "public/js/doctypelistJs.js"} 

# after_install = "apps.luggage_tracking.luggage_tracking.api.after_install"
