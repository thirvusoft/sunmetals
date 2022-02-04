import frappe
import re

def post(self, postal_code):
    if(self.pincode == None):
        frappe.throw("Please Enter the Postal Code.")
    else:
        postal_val = r"^[1-9][\d]{5}$"
        if(re.match(postal_val, self.pincode)):
            pass
        else:
            frappe.throw("Please Give the Correct Postal Code Format")



def phone(self, phone):
    pho = r"^[+][0-9]{2,3}[ ][0-9]{10}$"
    if(self.mobile_no == '+91 '):
        frappe.throw("Please Enter the Mobile Number.")
    else:
        if(re.match(pho,self.mobile_no)):
            pass
        else:
            frappe.throw("Please Enter the Correct Mobile Number")
    if(self.pincode == None):
        frappe.throw("Please Enter the Postal Code.")
    else:
        postal_val = r"^[1-9][\d]{5}$"
        if(re.match(postal_val, self.pincode)):
            pass
        else:
            frappe.throw("Please Give the Correct Postal Code Format")
    
    if(self.phone == '+91 '):
        pass
    elif(self.phone == None):
        pass
    else:
        if(re.match(pho,self.phone)):
            pass
        else:
            frappe.throw("Please Enter the Correct Phone Number")

    if(self.whatsapp_number == '+91 '):
        pass
    elif(self.whatsapp_number == None):
        pass
    else:
        if(re.match(pho,self.whatsapp_number)):
            pass
        else:
            frappe.throw("Please Enter the Correct Whatsapp Number")