import frappe
import re

def post(self, postal_code):
    if(self.pincode == None):
        frappe.throw("Please enter the postal code.")
    else:
        postal_val = r"^[1-9][\d]{5}$"
        if(re.match(postal_val, self.pincode)):
            pass
        else:
            frappe.throw("Please give the correct postal code format")
def phone(self, phone):
    pho = r"^[+][0-9]{2,3}[ ][0-9]{10}$";
    if(self.phone == '+91 '):
        pass
    elif(self.phone == None):
        pass
    else:
        if(re.match(pho,self.phone)):
            pass
        else:
            frappe.throw("Please enter the correct Phone Number")

    if(self.whatsapp_number == '+91 '):
        pass
    elif(self.whatsapp_number == None):
        pass
    else:
        if(re.match(pho,self.whatsapp_number)):
            pass
        else:
            frappe.throw("Please enter the correct Whatsapp Number")
    
    if(re.match(pho,self.mobile_no)):
        pass
    else:
        frappe.throw("Please enter the correct Mobile Number")
    if(self.pincode == None):
        frappe.throw("Please enter the postal code.")
    else:
        postal_val = r"^[1-9][\d]{5}$"
        if(re.match(postal_val, self.pincode)):
            pass
        else:
            frappe.throw("Please give the correct postal code format")
    