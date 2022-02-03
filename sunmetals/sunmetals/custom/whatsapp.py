import frappe
from frappe import _
from frappe.contacts.address_and_contact import load_address_and_contact
from erpnext.crm.doctype.lead.lead import Lead
from erpnext.controllers.selling_controller import SellingController
class Create_address(SellingController):
	def create_address(self):
		address_fields = ["address_type", "address_title", "address_line1", "address_line2",
			"city", "county", "state", "country", "pincode"]
		info_fields = ["email_id", "phone", "fax", "whatsapp_number", "gstin", "gst_state"]

		# do not create an address if no fields are available,
		# skipping country since the system auto-sets it from system defaults
		address = frappe.new_doc("Address")

		address.update({addr_field: self.get(addr_field) for addr_field in address_fields})
		address.update({info_field: self.get(info_field) for info_field in info_fields})
		address.insert()
		
		return address