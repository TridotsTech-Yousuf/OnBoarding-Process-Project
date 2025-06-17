// Copyright (c) 2025, Mohammed Yousuf and contributors
// For license information, please see license.txt

frappe.ui.form.on("Luggage Status Update", {
    refresh: function(frm) {
        $("[data-fieldname='passenger_name'] input").focus()
    },
    check_in_luggage_id: function(frm) {
        // When luggage_id is set, fetch the luggage details
        if (frm.doc.check_in_luggage_id) {
            frappe.call({
                method: "luggage_tracking.luggage_tracking.doctype.luggage_status_update.luggage_status_update.update_luggage_status_from_scan",
                args: {
                    check_in_luggage_id: frm.doc.check_in_luggage_id
                },
                callback: function(r) {
                    if (r.message) {
                        if (r.message == "Luggage not found") {
                            frappe.show_alert({
                                message: r.message,
                                indicator: 'red'
                            }, 3);
                        } else if (r.message == "No Luggage ID provided") {
                            frappe.show_alert({
                                message: r.message,
                                indicator: 'red'
                            }, 3);
                        }
                        frappe.show_alert({
                            message: r.message,
                            indicator: 'green'
                        }, 3);
                        reset_field(frm, "check_in_luggage_id");
                        focus_field(frm, "check_in_luggage_id");
                    }
                }
            });  
        }
    },
});

var reset_field = function(frm, fieldname) {
    frm.set_value(fieldname, "");
    frm.refresh_field(fieldname);
    $(`[data-fieldname="${fieldname}"] input`).focus();
};

var focus_field = function focus_field(frm, fieldname) {
    $(`[data-fieldname=${fieldname}] input`).focus()
}