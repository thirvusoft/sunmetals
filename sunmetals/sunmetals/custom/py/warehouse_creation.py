import frappe

def warehouse_creation_from_branch(self,event):
    if not self.warehouse:
        warehouse=frappe.new_doc("Warehouse")
        warehouse.update({
                    'doctype':'Warehouse',
                    'warehouse_name':self.name,
                    'branch':self.name,
                    "parent_warehouse":f"All Warehouses - {self.abbr}"
                })
        warehouse.flags.ignore_mandatory=True
        
        warehouse.insert(ignore_permissions=True)
        self.warehouse=warehouse.name
        self.save()
