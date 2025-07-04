// Copyright (c) 2025, Mohammed Yousuf and contributors
// For license information, please see license.txt

frappe.ui.form.on("FRM AND Frappe Example", {
	refresh(frm) {

        frm.add_custom_button("BTN 1",()=>{
            // Normal (or) Simple Structure
            frm.call("greet");
        });

        frm.add_custom_button("BTN 2",()=>{
            // Adding .then after calling
            frm.call('greet') // Front End la irundhu greet apdnra method'a kupudrom inga vaa apdnu.
            .then(response => { // namba kuptadhukaana response idhula dha varum. adha namba some parameter name la vangi keela manipulate panrom.
                if (response) {
                  console.log(response);// for example naa greet apdnra method'a kuptu iruken. adhu yenaku inga varudhu. adha naa response apdnra perla vaangi , indha line la summa yenna varudhu nu browser la print panni paakuren.
                }
            })
        });

        // Note: Instead of .then we can also use callback.

        // frm.call ooda full structure (inside frm.call)
        frm.add_custom_button("BTN 3",()=>{
            frm.call({
                method: "greet",      // Required — either class method or whitelisted function
                args: {                     // Optional — values you want to pass to the backend
                    static_name: frm.doc.name1,
                    // we can give many args as we want
                },
                doc: frm.doc,               // Optional — sends entire document if needed
                freeze: true,               // Optional — shows "Please Wait" loader
                freeze_message: "Loading",  // Optional — custom loading message
                callback: function(r) {     // Required — what to do when response comes back
                    // r.message contains return value from backend
                    console.log(r.message);
                },
                error: function(r) {        // Optional — what to do on error
                    console.error("Error occurred", r);
                },
                always: function(r) {       // Optional — runs whether success or error
                    console.log("Done (success or fail)");
                }
            });
        })

        //

	},
});
