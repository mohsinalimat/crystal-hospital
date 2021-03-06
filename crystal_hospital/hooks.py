# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "crystal_hospital"
app_title = "Crystal Hospital"
app_publisher = "4C Solutions"
app_description = "Crystal Hospital Customizations"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@4csolutions.in"
app_license = "MIT"

fixtures = [    
    {
        "doctype": "Role Profile",
        "filters" : [
            [
                "name",
                "in",
                [
                    "CMH Manager",
                    "CMH Reception"
                ]
            ]
        ]
    },
    {
        "doctype": "Role",
        "filters" : [
            [
                "name",
                "in",
                [
                    "CMH Manager",
                    "CMH Reception"
                ]
            ]
        ]
    }
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/crystal_hospital/css/crystal_hospital.css"
# app_include_js = "/assets/crystal_hospital/js/crystal_hospital.js"

# include js, css files in header of web template
# web_include_css = "/assets/crystal_hospital/css/crystal_hospital.css"
# web_include_js = "/assets/crystal_hospital/js/crystal_hospital.js"

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

# Home Pages
# ----------

# application home page (will override Website Settings)
home_page = "index"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "crystal_hospital.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "crystal_hospital.install.before_install"
# after_install = "crystal_hospital.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "crystal_hospital.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

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
# 		"crystal_hospital.tasks.all"
# 	],
# 	"daily": [
# 		"crystal_hospital.tasks.daily"
# 	],
# 	"hourly": [
# 		"crystal_hospital.tasks.hourly"
# 	],
# 	"weekly": [
# 		"crystal_hospital.tasks.weekly"
# 	]
# 	"monthly": [
# 		"crystal_hospital.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "crystal_hospital.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "crystal_hospital.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "crystal_hospital.task.get_dashboard_data"
# }
override_whitelisted_methods = {
    "erpnext.healthcare.utils.get_healthcare_services_to_invoice": "crystal_hospital.utils.get_healthcare_services_to_invoice"
}
# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

jenv = {
    "methods": [
        "format_duration:frappe.utils.format_duration",
        "time_diff_in_seconds:frappe.utils.time_diff_in_seconds"
    ]
}