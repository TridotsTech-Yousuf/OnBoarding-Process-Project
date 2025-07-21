// Copyright (c) 2025, Mohammed Yousuf and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Chat GPT", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('Chat GPT', {
    refresh: function(frm) {
        frm.add_custom_button('🎤 Speak Prompt', () => {
            if (!('webkitSpeechRecognition' in window)) {
                frappe.msgprint("Voice recognition not supported in this browser.");
                return;
            }

            let recognition = new webkitSpeechRecognition();
            recognition.lang = 'en-US';
            recognition.interimResults = false;
            recognition.maxAlternatives = 1;

            // frappe.msgprint("🎙️ Speak now...");
            frappe.show_alert({
                message:__('Speak Now'),
                indicator:'green'
            }, 10);

            recognition.onresult = function(event) {
                const transcript = event.results[0][0].transcript;
                frm.set_value('prompt', transcript);
                frm.save();
            };

            recognition.onerror = function(event) {
                frappe.msgprint("❌ Error: " + event.error);
            };

            recognition.start();
        });
    }
});

