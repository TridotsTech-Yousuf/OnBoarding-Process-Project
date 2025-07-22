// // Copyright (c) 2025, Mohammed Yousuf and contributors
// // For license information, please see license.txt

// // frappe.ui.form.on("Chat GPT", {
// // 	refresh(frm) {

// // 	},
// // });

// // frappe.ui.form.on('Chat GPT', {
// //     refresh: function(frm) {
// //         frm.add_custom_button('🎤 Speak Prompt', () => {
// //             if (!('webkitSpeechRecognition' in window)) {
// //                 frappe.msgprint("Voice recognition not supported in this browser.");
// //                 return;
// //             }

// //             let recognition = new webkitSpeechRecognition();
// //             recognition.lang = 'en-US';
// //             recognition.interimResults = false;
// //             recognition.maxAlternatives = 1;

// //             // frappe.msgprint("🎙️ Speak now...");
// //             frappe.show_alert({
// //                 message:__('Speak Now'),
// //                 indicator:'green'
// //             }, 10);

// //             recognition.onresult = function(event) {
// //                 const transcript = event.results[0][0].transcript;
// //                 frm.set_value('prompt', transcript);
// //                 frm.save();
// //             };

// //             recognition.onerror = function(event) {
// //                 frappe.msgprint("❌ Error: " + event.error);
// //             };

// //             recognition.start();
// //         });
// //     }
// // });

// frappe.ui.form.on('Chat GPT', {
//     refresh(frm) {
//         frm.add_custom_button("💬 Chat", () => {
//             show_chat_modal();
//         });
//     }
// });

// function show_chat_modal() {
//     let d = new frappe.ui.Dialog({
//         title: "🤖 Talk to ERP Chatbot",
//         fields: [
//             {
//                 label: "Your Message",
//                 fieldname: "message",
//                 fieldtype: "Small Text"
//             }
//         ],
//         primary_action_label: "Send",
//         primary_action(values) {
//             frappe.call({
//                 method: "luggage_tracking.luggage_tracking.doctype.chat_gpt.chat_gpt.chat_with_gpt",
//                 args: { prompt: values.message },
//                 callback(r) {
//                     frappe.msgprint("💬 Response: " + r.message);
//                 }
//             });
//             d.hide();
//         }
//     });
//     d.show();
// }

frappe.ui.form.on('Chat GPT', {
    refresh(frm) {
        frm.add_custom_button('🎤 Speak Prompt', () => {
            if (!('webkitSpeechRecognition' in window)) {
                frappe.msgprint("Voice recognition not supported in this browser.");
                return;
            }

            let recognition = new webkitSpeechRecognition();
            recognition.lang = 'en-US';
            recognition.interimResults = false;
            recognition.maxAlternatives = 1;

            frappe.show_alert({
                message: __('🎙️ Speak Now'),
                indicator: 'green'
            }, 10);

            recognition.onresult = function (event) {
                const transcript = event.results[0][0].transcript;
                frm.set_value('prompt', transcript);
                frm.save();
            };

            recognition.onerror = function (event) {
                frappe.msgprint("❌ Error: " + event.error);
            };

            recognition.start();
        });

        frm.add_custom_button("💬 Chat", () => {
            show_chat_modal();
        });
    }
});

function show_chat_modal() {
    let d = new frappe.ui.Dialog({
        title: "🤖 Talk to ERP Chatbot",
        fields: [
            {
                label: "Your Message",
                fieldname: "message",
                fieldtype: "Small Text"
            }
        ],
        primary_action_label: "Send",
        primary_action(values) {
            frappe.call({
                method: "luggage_tracking.luggage_tracking.doctype.chat_gpt.chat_gpt.chat_with_gpt",
                args: { prompt: values.message },
                callback(r) {
                    frappe.msgprint({
                        title: __("Bot Response"),
                        message: r.message,
                        indicator: 'green'
                    });
                }
            });
            d.hide();
        }
    });
    d.show();
}
