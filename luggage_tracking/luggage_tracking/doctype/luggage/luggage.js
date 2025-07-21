// frappe.ui.form.on("Luggage", {
// 	refresh(frm) {


// 		// Go to Passenger Verification
// 		frm.add_custom_button("Go to Passenger Verification", function () {
// 			frappe.set_route("List", "Passenger Verification");
// 		});

// 		// Download Tag
// 		frm.add_custom_button("Download Tag", () => {
// 			let passenger_name = frm.doc.passenger_name;
// 			if (passenger_name) {
// 				window.open(`/api/method/luggage_tracking.luggage_tracking.doctype.luggage.luggage.download_luggage_tag?passenger_name=${passenger_name}`);
// 			} else {
// 				frappe.msgprint("Passenger Name not set");
// 			}
// 		});

// 		// Show Make Payment only if extra luggage exists AND payment not made
// 		if (frm.doc.extra_luggage && frm.doc.payment_status !== "Paid") {
// 			add_payment_button(frm);
// 		} else {
// 			frm.remove_custom_button("Make Payment");
// 		}
// 	},

// 	extra_luggage(frm) {
// 		if (frm.doc.extra_luggage == 1 && frm.doc.payment_status !== "Paid") {
// 			add_payment_button(frm);
// 		} else {
// 			frm.remove_custom_button("Make Payment");
// 		}
// 	},

// 	onload(frm) {
// 		calculate_total_weight(frm);
// 	},

// 	luggage_details_add(frm) {
// 		calculate_total_weight(frm);
// 	},

// 	luggage_details_remove(frm) {
// 		calculate_total_weight(frm);
// 	}
// });

// frappe.ui.form.on("Luggage Details", {
// 	weight(frm, cdt, cdn) {
// 		calculate_total_weight(frm);		
// 		if(frm.doc.luggage_details[0]){
// 			console.log("Yes")
// 		} else {
// 			console.log("No");
// 		}
// 	},
// 	luggage_type(frm, cdt, cdn) {
// 		calculate_total_weight(frm);
// 	}
// });

// function calculate_total_weight(frm) {
// 	let total_weight = 0;
// 	let check_in_weight = 0;
// 	let cabin_weight = 0;

// 	(frm.doc.luggage_details || []).forEach(row => {
// 		let weight = row.weight || 0;
// 		total_weight += weight;

// 		if (row.luggage_type === "Check IN") {
// 			check_in_weight += weight;
// 		} else if (row.luggage_type === "Cabin") {
// 			cabin_weight += weight;
// 		}
// 	});

// 	const additional_check_in = check_in_weight > 25 ? check_in_weight - 25 : 0;
// 	const additional_cabin = cabin_weight > 7 ? cabin_weight - 7 : 0;

// 	frm.set_value("total_weight", total_weight);
// 	frm.set_value("additional_check_in_luggage_weight", additional_check_in);
// 	frm.set_value("additional_cabin_luggage_weight", additional_cabin);
// }

// function add_payment_button(frm) {
// 	frm.remove_custom_button("Make Payment");

// 	frm.add_custom_button("Make Payment", () => {
// 		let amount = (frm.doc.additional_check_in_luggage_weight * 10000) +
// 		             (frm.doc.additional_cabin_luggage_weight * 10000);

// 		if (amount <= 0) {
// 			frappe.msgprint("No additional luggage to charge.");
// 			return;
// 		}

// 		let options = {
// 			key: "rzp_test_1DP5mmOlF5G5ag",
// 			amount: amount,
// 			currency: "INR",
// 			name: frm.doc.passenger_name || "Demo User",
// 			description: "Extra Luggage Payment",
// 			handler: function (response) {
// 				frm.set_value("payment_id", response.razorpay_payment_id);
// 				frm.set_value("payment_status", "Paid");
// 				frm.remove_custom_button("Make Payment");
// 			},
// 			prefill: {
// 				name: frm.doc.passenger_name || "Test User",
// 				email: frm.doc.email || "test@example.com",
// 				contact: frm.doc.phone_number || "9999999999"
// 			},
// 			theme: {
// 				color: "#3399cc"
// 			},
// 			modal: {
// 				ondismiss: function () {
// 					frappe.msgprint("You closed the Razorpay popup.");
// 				}
// 			}
// 		};

// 		let rzp = new Razorpay(options);
// 		rzp.open();
// 	});
// }

frappe.ui.form.on("Luggage", {
	refresh(frm) {
		// Go to Passenger Verification
		frm.add_custom_button("Go to Passenger Verification", function () {
			frappe.set_route("List", "Passenger Verification");
		});

		// Download Tag
		frm.add_custom_button("Download Tag", () => {
			let passenger_name = frm.doc.passenger_name;
			if (passenger_name) {
				window.open(`/api/method/luggage_tracking.luggage_tracking.doctype.luggage.luggage.download_luggage_tag?passenger_name=${passenger_name}`);
			} else {
				frappe.msgprint("Passenger Name not set");
			}
		});

		// Show Make Payment only if extra luggage exists AND payment not made
		if (frm.doc.extra_luggage && frm.doc.payment_status !== "Paid") {
			add_payment_button(frm);
		} else {
			frm.remove_custom_button("Make Payment");
		}

		// Check for child table rows and toggle Save button
		toggle_save_button(frm);
	},

	before_save(frm){
		var luggage_details = frm.doc.luggage_details
		luggage_details.forEach(function(item, index) {
			if(item.luggage_type && !item.weight){
				frappe.msgprint("Please Enter weight");
			} else if( !(item.luggage_type) && item.weight) {
				frappe.msgprint("Please Enter Luggage Type");
			}
		});
	},

	extra_luggage(frm) {
		if (frm.doc.extra_luggage == 1 && frm.doc.payment_status !== "Paid") {
			add_payment_button(frm);
		} else {
			frm.remove_custom_button("Make Payment");
		}
	},

	onload(frm) {
		calculate_total_weight(frm);
		toggle_save_button(frm);
	},

	luggage_details_add(frm) {
		calculate_total_weight(frm);
		toggle_save_button(frm);
	},

	luggage_details_remove(frm) {
		calculate_total_weight(frm);
		toggle_save_button(frm);
	},
});

// Child Table Logic
frappe.ui.form.on("Luggage Details", {
	weight(frm, cdt, cdn) {
		calculate_total_weight(frm);
		toggle_save_button(frm);
	},
	luggage_type(frm, cdt, cdn) {
		calculate_total_weight(frm);
	},
});

// Utility to calculate weight
function calculate_total_weight(frm) {
	let total_weight = 0;
	let check_in_weight = 0;
	let cabin_weight = 0;

	(frm.doc.luggage_details || []).forEach(row => {
		let weight = row.weight || 0;
		total_weight += weight;

		if (row.luggage_type === "Check IN") {
			check_in_weight += weight;
		} else if (row.luggage_type === "Cabin") {
			cabin_weight += weight;
		}
	});

	const additional_check_in = check_in_weight > 25 ? check_in_weight - 25 : 0;
	const additional_cabin = cabin_weight > 7 ? cabin_weight - 7 : 0;

	frm.set_value("total_weight", total_weight);
	frm.set_value("additional_check_in_luggage_weight", additional_check_in);
	frm.set_value("additional_cabin_luggage_weight", additional_cabin);
}

// Razorpay Integration
function add_payment_button(frm) {
	frm.remove_custom_button("Make Payment");

	frm.add_custom_button("Make Payment", () => {
		let amount = (frm.doc.additional_check_in_luggage_weight * 10000) +
		             (frm.doc.additional_cabin_luggage_weight * 10000);

		if (amount <= 0) {
			frappe.msgprint("No additional luggage to charge.");
			return;
		}

		let options = {
			key: "rzp_test_1DP5mmOlF5G5ag",
			amount: amount,
			currency: "INR",
			name: frm.doc.passenger_name || "Demo User",
			description: "Extra Luggage Payment",
			handler: function (response) {
				frm.set_value("payment_id", response.razorpay_payment_id);
				frm.set_value("payment_status", "Paid");
				frm.remove_custom_button("Make Payment");
			},
			prefill: {
				name: frm.doc.passenger_name || "Test User",
				email: frm.doc.email || "test@example.com",
				contact: frm.doc.phone_number || "9999999999"
			},
			theme: {
				color: "#3399cc"
			},
			modal: {
				ondismiss: function () {
					frappe.msgprint("You closed the Razorpay popup.");
				}
			}
		};

		let rzp = new Razorpay(options);
		rzp.open();
	});
}

// Show Save button only if child table has rows
function toggle_save_button(frm) {
	if (frm.doc.luggage_details && frm.doc.total_weight > 0 ) {
		 frm.enable_save();
	} else {
		frm.disable_save();
	}
}
