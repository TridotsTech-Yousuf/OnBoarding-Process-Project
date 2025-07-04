// Copyright (c) 2025, Mohammed Yousuf and contributors
// For license information, please see license.txt

frappe.ui.form.on("Form API", {
	refresh(frm) {
        
        // Set Value: - Working

        // frm.set_value('description', 'hhfhtfhtftfh')         // set a single value  
        // frm.refresh_field("description")
        // frm.set_value('description', 'mmmmmmmmmmmm') 


        // frm.set_value({
        //     status: "Demo",
        //     checked: 1
        // })                                                      // set multiple values at once

        
        // frm.set_value('description', 'New description with promise')
        //     .then(() => {
        //        frappe.msgprint("Set Value Method Called !!!")
        //     }
        // )                                                     

        // ---------------------------------------------------------------------------------------------------------------------

        // Refresh: - Not Working

        // frm.add_custom_button("Refresh",()=>{
        //     frm.refresh();
        //     // frappe.msgprint("Refreshed")
        // });

        // ---------------------------------------------------------------------------------------------------------------------

        // Save:

        // frm.add_custom_button("Custom Save",()=>{
        //     frm.save();
        //     frm.set_value('status', 'Custom Save Triggered')
        //     frappe.show_alert({
        //         message:('Save Button Clicked'),
        //         indicator:'yellow'
        //     }, 5);
        // });

        // Submit
        // frm.add_custom_button("Custom Submit",()=>{
        //     frm.save("Submit");
        //     frm.set_value('status', 'Custom Submit Triggered')
        //     frappe.show_alert({
        //         message:('Submit Button Clicked'),
        //         indicator:'yellow'
        //     }, 5);
        // });

        // Cancel
        // frm.add_custom_button("Custom Cancel",()=>{
        //     frm.save("Cancel");
        //     frm.set_value('status', 'Custom Cancel Triggered')
        //     frappe.show_alert({
        //         message:('Cancel Button Clicked'),
        //         indicator:'yellow'
        //     }, 5);
        // });

        // Update
        // frm.add_custom_button("Custom Update",()=>{
        //     frm.save("Update");
        //     frm.set_value('status', 'Custom Update Triggered')
        //     frappe.show_alert({
        //         message:('Update Button Clicked'),
        //         indicator:'yellow'
        //     }, 5);
        // });

        // ---------------------------------------------------------------------------------------------------------------------

        // Email Doc

        // frm.add_custom_button("Email Doc",()=>{
        //     frm.email_doc();
        //     frappe.show_alert({
        //         message:('Email Doc Clicked'),
        //         indicator:'yellow'
        //     }, 5);
        // });

        // ---------------------------------------------------------------------------------------------------------------------

        // Reload Doc - Working

        // frm.add_custom_button("Reload Doc",()=>{
        //     frm.reload_doc();
        //     frappe.show_alert({
        //         message:('Reload Doc Clicked'),
        //         indicator:'yellow'
        //     }, 5);
        // });

        // ---------------------------------------------------------------------------------------------------------------------

        // Refresh Field - Not Working

        // frm.add_custom_button("Refresh Field",()=>{
        //     frm.refresh_field('name1');
        //     frm.refresh_field('description');
        //     frappe.show_alert({
        //         message:('Refresh Field Clicked'),
        //         indicator:'yellow'
        //     }, 5);
        // });
        
        // ---------------------------------------------------------------------------------------------------------------------

        // Is Dirty - Working

        // frm.add_custom_button("Is Dirty",()=>{
        //      if (frm.is_dirty()) {
        //         frappe.show_alert('Form is Dirty')
        //     } else {
        //         frappe.show_alert('Form is Not Dirty')
        //     }
        // });

        // ---------------------------------------------------------------------------------------------------------------------

        // Is New - Working

        // frm.add_custom_button("Is New",()=>{
        //      if (frm.is_new()) {
        //         frappe.show_alert('Form is New')
        //     } else {
        //         frappe.show_alert('Form is Not New')
        //     }
        // });

        // Change Custom Button Type - Working

        // frm.change_custom_button_type('Is New', null, 'warning'); // Button Label, Group Label, Button Type(Primary, Danger, Success, Warning)
        // frm.change_custom_button_type('Closed', 'status', 'danger');

        // Remove Custom Button - Working

        // frm.add_custom_button("Remove Is New Button",()=>{
        //     frm.remove_custom_button("Is New");
        // })

        // Clear Custom Buttons - Working
        // show_button_1(frm);


        // ---------------------------------------------------------------------------------------------------------------------

        // Set Intro - Wroking

        // if (!frm.doc.description) {
            // frm.set_intro('Please set the value of description');
        // }

        // if (!frm.doc.description) {
            // frm.set_intro('Welcome to document', 'blue');
        // }

        // ---------------------------------------------------------------------------------------------------------------------

        // Trigger

        // frm.add_custom_button("FRM Trigger",()=>{
        //     frm.trigger('checked');
        // })

	},

        // Toggle 

        // checked(frm) {
        //     frm.toggle_reqd("description", true);  
        // }

    // ---------------------------------------------------------------------------------------------------------------------

    // Enable Save and Disable Save - Working
 
    // checked(frm){
    //     if(frm.doc.checked){
    //         frm.disable_save();
    //     } else {
    //         frm.enable_save();
    //     }
    // },

    // ---------------------------------------------------------------------------------------------------------------------

    // Set DF Property - Working

    // checked(frm){
    //     if(frm.doc.checked){
    //         frm.set_df_property('description', 'reqd', 1)
    //         frm.set_df_property('description', 'fieldtype', 'Text Editor');
    //     } else {
    //         frm.set_df_property('description', 'reqd', 0)
    //     }
    // },

    // ---------------------------------------------------------------------------------------------------------------------

    // Toogle Enable - Working

    // checked(frm) {
    //     if (frm.doc.checked) {
    //         frm.toggle_enable("description", false);  // Enable the field
    //     } else {
    //         frm.toggle_enable("description", true); // Disable the field
    //     }
    // }

    // ---------------------------------------------------------------------------------------------------------------------

    // Toggle Reqd - Working

    // checked(frm) {
    //     if (frm.doc.checked) {
    //         frm.toggle_reqd("description", true);  
    //     } else {
    //         frm.toggle_reqd("description", false); 
    //     }
    // }

    // ---------------------------------------------------------------------------------------------------------------------

    // Toggle Display - Working

    // checked(frm) {
    //     if (frm.doc.checked) {
    //         frm.toggle_display("description", false); 
    //     } else {
    //         frm.toggle_display("description", true); 
    //     }
    // }

    // ---------------------------------------------------------------------------------------------------------------------


});

// function show_button_1(frm) {
//     frm.clear_custom_buttons();
//     frm.add_custom_button("Button 1", () => {
//         show_button_2(frm);
//     });
// }

// function show_button_2(frm) {
//     frm.clear_custom_buttons();
//     frm.add_custom_button("Button 2", () => {
//         show_button_1(frm);
//     });
// }

