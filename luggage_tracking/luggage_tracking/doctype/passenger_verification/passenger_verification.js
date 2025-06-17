frappe.ui.form.on("Passenger Verification", {
    is_verified(frm) {
        if (frm.doc.is_verified == 1) {
            frappe.confirm(
                __('Are you sure, all details verified?'),
                function () {
                    frm.set_value('is_verified', 1);

                    frm.fields.forEach(field => {
                        if (field.df.fieldname !== 'is_verified') {
                            frm.set_df_property(field.df.fieldname, 'read_only', 1);
                        }
                    });

                    frappe.show_alert({
                        message: __('Verification successful'),
                        indicator: 'green'
                    }, 5);
                },
                function () {
                    frm.set_value('is_verified', 0);
                }
            );
        } else {
            frm.fields.forEach(field => {
                if (field.df.fieldname !== 'is_verified') {
                    frm.set_df_property(field.df.fieldname, 'read_only', 0);
                }
            });

            frappe.show_alert({
                message: __('Verification cancelled'),
                indicator: 'red'
            }, 5);
        }
    },
    refresh(frm) {
        if (frm.doc.is_verified == 1) {
            frm.add_custom_button(__('Add Luggage'), function() {
                frappe.route_options = {
                    passenger_name: frm.doc.passenger_name,
                    e_ticket_number:frm.doc.e_ticket_number,
                    phone_number: frm.doc.phone_number,
                    email: frm.doc.email,
                };
                frappe.set_route('Form', 'Luggage', 'new-luggage-1');
            });

            frm.add_custom_button('Check Luggage Status', () => {
                frappe.call({
                    method: "luggage_tracking.api.search_luggage", 
                    args: {
                        passenger_name: frm.doc.passenger_name
                    },
                    callback: function(r) {
                        if (r.message.status === "ok") {
                            frappe.show_alert({
                                message: "Luggage Found ✅",
                                indicator: 'green'
                            }, 5);
                        } else {
                            frappe.show_alert({
                                message: "Luggage Not Found ❌",
                                indicator: 'red'
                            }, 5);
                        }
                    }
                });
            });
        }
        
        frm.add_custom_button(__("Get Verified Passengers List"), function () {
            frappe.call({
                method: "luggage_tracking.luggage_tracking.doctype.passenger_verification.passenger_verification.get_verified_passenger_luggage",
                callback: function (r) {
                    if (r.message && r.message.status === "success") {
                        frappe.msgprint("Passengers List Printed");
                    } else if (r.message && r.message.status === "failed") {
                        frappe.msgprint("No Passengers Found");
                    } else {
                        frappe.msgprint("Error");
                    }
                }
            });
        });
    }
});

// Dialog API
// let d = new frappe.ui.Dialog({
//     title: 'Enter details',
//     fields: [
//         {
//             label: 'First Name',
//             fieldname: 'first_name',
//             fieldtype: 'Data'
//         },
//     ],
//     size: 'small', // small, large, extra-large 
//     primary_action_label: 'Submit',
//     primary_action(values) {
//         console.log(values);
//         d.hide();
//     }
// });

// d.show();


