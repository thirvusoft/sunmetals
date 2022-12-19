from . import __version__ as app_version

app_name = "sunmetals"
app_title = "Sunmetals"
app_publisher = "Thirvusoft"
app_description = "Manufacturer of Aluminium Products"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "sunbrandindia@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sunmetals/css/sunmetals.css"
# app_include_js = "/assets/sunmetals/js/sunmetals.js"

# include js, css files in header of web template
# web_include_css = "/assets/sunmetals/css/sunmetals.css"
# web_include_js = "/assets/sunmetals/js/sunmetals.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "sunmetals/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views

doctype_js = {"Customer" : "sunmetals/custom/js/customer.js",
			 "Delivery Note": "sunmetals/custom/js/delivery_note.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "sunmetals.install.before_install"
# after_install = "sunmetals.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sunmetals.notifications.get_notification_config"

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
override_doctype_class = {
	"Lead":"sunmetals.sunmetals.custom.py.lead.CustomLead"
}

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events
doc_events = {
    
    "Lead": {
        "validate":"sunmetals.sunmetals.custom.py.validation.phone",
    },
	"Address":{
		"validate":"sunmetals.sunmetals.custom.py.validation.post",
	},
	"User":{
		"on_update":"sunmetals.sunmetals.custom.py.user_permission.create_user_permission",
	},
	"Branch":{
		"on_update":"sunmetals.sunmetals.custom.py.warehouse_creation.warehouse_creation_from_branch"
	}
#   "Item": {
#       "autoname": "tshotel.tshotel.custom.Python.Postcode.set_si_autoname"
#   }
}

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"sunmetals.tasks.all"
# 	],
# 	"daily": [
# 		"sunmetals.tasks.daily"
# 	],
# 	"hourly": [
# 		"sunmetals.tasks.hourly"
# 	],
# 	"weekly": [
# 		"sunmetals.tasks.weekly"
# 	]
# 	"monthly": [
# 		"sunmetals.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "sunmetals.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "sunmetals.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "sunmetals.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"sunmetals.auth.validate"
# ]

