from erpnext.crm.doctype.lead.lead import Lead
import frappe
from frappe import _
from frappe.contacts.address_and_contact import load_address_and_contact
from frappe.email.inbox import link_communication_to_document
from frappe.model.mapper import get_mapped_doc
from frappe.utils import comma_and, cstr, getdate, has_gravatar, nowdate, validate_email_address
from erpnext.accounts.party import set_taxes
from erpnext.controllers.selling_controller import SellingController
from frappe.contacts.doctype.address.address import (
    Address,
    get_address_display,
    get_address_templates,
)
class CustomLead(Lead):
    # def validate(self):
    #     self.create_address()
    def create_address(self):
        address_fields = ["address_type", "address_title", "address_line1", "address_line2",
            "city", "county", "state", "country", "pincode", "postal_code"]
        info_fields = ["email_id", "phone", "fax", "gstin", "gst_state","whatsapp_number"]
        # do not create an address if no fields are available,
        # skipping country since the system auto-sets it from system defaults
        address = frappe.new_doc("Address")
        address.update({addr_field: self.get(addr_field) for addr_field in address_fields})
        address.update({info_field: self.get(info_field) for info_field in info_fields})
        address.insert()
        return address