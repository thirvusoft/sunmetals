frappe.ui.form.on("Customer", {
    onload:function(frm){
        frm.set_query('parent_customer', function(doc) {
			return {
				filters: {
					"is_parent": 1
				}
			};
		});
    }
})