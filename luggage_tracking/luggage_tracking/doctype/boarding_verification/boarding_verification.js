frappe.ui.form.on("Boarding Verification", {
    refresh: function(frm) {
        $("[data-fieldname='passenger_name'] input").focus()
    },
    passenger_name: function(frm) {
        if (frm.doc.passenger_name) {
            frappe.call({
                method: "luggage_tracking.luggage_tracking.doctype.boarding_verification.boarding_verification.fetch_boarding_verification_data",
                args: {
                    passenger_name: frm.doc.passenger_name
                },
                callback: function(r) {
                    if (r.message) {
                        frm.set_value("seat_number", r.message.seat_number);
                        frm.set_value("is_verified", r.message.is_verified);
                        frm.set_value("e_ticket_number", r.message.e_ticket_number);
                        frm.set_value("status", r.message.status);
                        frm.set_value("class_of_service", r.message.class_of_service);
                        frm.set_value("boarded", r.message.boarded);

                        frappe.show_alert({
                            message: frm.doc.passenger_name + " Boarded",
                            indicator: 'green'
                        }, 3);

                        frappe.call({
                            method: "luggage_tracking.luggage_tracking.doctype.boarding_verification.boarding_verification.create_boarded_passenger",
                            args: {
                                data: JSON.stringify({
                                    passenger_name: frm.doc.passenger_name,
                                    seat_number: r.message.seat_number,
                                    is_verified: r.message.is_verified,
                                    e_ticket_number: r.message.e_ticket_number,
                                    status: r.message.status,
                                    class_of_service: r.message.class_of_service,
                                    boarded: r.message.boarded
                                })
                            },
                            callback: function(res) {
                                frappe.show_alert({
                                    message: "Boarded Passenger record created:" + res.message,
                                    indicator: 'green'
                                }, 3);
                            }
                        });

                        setTimeout(function() {
                            reset_field(frm, "passenger_name");
                            reset_field(frm, "seat_number");
                            reset_field(frm, "is_verified");
                            reset_field(frm, "e_ticket_number");
                            reset_field(frm, "status");
                            reset_field(frm, "class_of_service");
                            reset_field(frm, "boarded");
                            focus_field(frm, "passenger_name");
                        }, 3000);

                    } else {
                        frappe.msgprint(__("Passenger Verification not found"));
                        frappe.show_alert({
                            message: frm.doc.passenger_name + " Not Boarded",
                            indicator: 'red'
                        }, 3);
                    }
                }
            });
        }
    }
});

var reset_field = function(frm, fieldname) {
    frm.set_value(fieldname, "");
    frm.refresh_field(fieldname);
    $(`[data-fieldname="${fieldname}"] input`).focus();
};

var focus_field = function focus_field(frm, fieldname) {
    $(`[data-fieldname=${fieldname}] input`).focus()
}