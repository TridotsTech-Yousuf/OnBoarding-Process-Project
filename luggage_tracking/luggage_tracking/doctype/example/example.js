frappe.ui.form.on("Example", {
	refresh(frm) {

        // Calling an api inside the doctype class. using frm.call
        frm.add_custom_button("BTN 1",()=>{
            frm.call("greet");
        });

        // Calling an api outide the doctype class. using frm.call
        frm.add_custom_button("BTN 2",()=>{
            frm.call("scold");
        });

        // Calling an api inside the doctype class. using frappe.call
        frm.add_custom_button("BTN 3",()=>{
            frappe.call({
                method: "luggage_tracking.luggage_tracking.doctype.example.example.greet"
            });
        });

        // Calling an api outide the doctype class. using frappe.call
        frm.add_custom_button("BTN 4",()=>{
            frappe.call({
                method: "luggage_tracking.luggage_tracking.doctype.example.example.scold"
            });
        });

        // Calling an api outide the doctype class. using frappe.call
        frm.add_custom_button("Upside",()=>{
            frappe.call({
                method: "luggage_tracking.luggage_tracking.doctype.example.example.sleep"
            });
        });
	},
});
