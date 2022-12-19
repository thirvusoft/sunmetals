import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.permissions import add_user_permission

def create_user_permission(doc,event):
    if doc.branch and not frappe.get_all("User Permission",{
        'user': doc.name, 
        'allow': "Branch", 
        "for_value": doc.branch, 
        "apply_to_all_doctypes": 1
    }):
        doc1=frappe.get_doc({
            'doctype':'User Permission',
            'user': doc.name, 
            'allow': "Branch", 
            "for_value": doc.branch, 
            "apply_to_all_doctypes": 1
        })
        doc1.flags.ignore_mandatory=True
        doc1.flags.ignore_permissions=True
        doc1.save()
    other_doc = frappe.get_all("User Permission",{'user': doc.name, 'allow': "Branch", "for_value": ["!=", doc.branch]}, pluck="name")
    for doc in other_doc:
        frappe.delete_doc("User Permission", doc)
