// console.log("App Included Called ...................................................................................... ")

frappe.show_alert("App Included...");

// frappe.ready(() => {
//     console.log("✅ webform_include.js loaded!");
//     frappe.msgprint("This is from webform_include.js!");
// });

frappe.ready(() => {
    if (!frappe.boot.sounds) frappe.boot.sounds = [];

    frappe.boot.sounds.push({
        name: "shot",
        src: "/assets/luggage_tracking/shot.mp3",
        volume: 0.5
    });

    // Trigger the sound (for test)
    frappe.msgprint("Sound will play now!");
    frappe.utils.play_sound("shot");
});
