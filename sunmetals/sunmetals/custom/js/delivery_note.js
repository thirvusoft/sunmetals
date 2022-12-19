console.log("PPPPPPP")
frappe.ui.form.on("Delivery Note", {   
   
    refresh(frm) {
        console.log("A")
		
        console.log("11")
		if ((!frm.doc.is_return) && (frm.doc.status!="Closed" || frm.is_new())) {
			if (frm.doc.docstatus==0) {
                console.log("22")
				frm.add_custom_button(__('Material Request'),
					function() {
						if (!me.frm.doc.customer) {
							frappe.throw({
								title: __("Mandatory"),
								message: __("Please Select a Customer")
							});
						}
						erpnext.utils.map_current_doc({
							method: "sunmetals.sunmetals.custom.py.delivery_note.make_delivery_note",
							source_doctype: "Material Request",
							target: me.frm,
							setters: {
								customer: me.frm.doc.customer,
							},
							get_query_filters: {
								docstatus: 1,
								status: ["not in", ["Closed", "On Hold"]],
								per_delivered: ["<", 99.99],
								company: me.frm.doc.company,
								project: me.frm.doc.project || undefined,
							}
						})
					}, __("Get Items From"));
			}
		}
    }

})