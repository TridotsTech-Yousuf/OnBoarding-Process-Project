// frappe.pages['chatbot'].on_page_load = function(wrapper) {
//     var page = frappe.ui.make_app_page({
//         parent: wrapper,
//         title: 'Chatbot',
//         single_column: true
//     });

//     $(wrapper).find('.layout-main-section').html(`
//         <div>
//             <input type="text" id="user_input" placeholder="Type your question..." style="width:70%" />
//             <button id="ask_btn" class="btn btn-primary">Ask</button>
//             <button id="clear_btn" class="btn btn-danger">Clear</button>
//             <div id="chat_output" style="margin-top:20px; white-space: pre-wrap; max-height: 400px; overflow-y: auto; border: 1px solid #ddd; padding: 10px; border-radius: 8px;"></div>
//         </div>
//     `);

//     // Ask button handler
//     $('#ask_btn').on('click', function() {
//         let question = $('#user_input').val().trim();
//         if (!question) return;

//         $('#chat_output').append(`<div><b>You:</b> ${question}</div>`);
//         $('#chat_output').append(`<div><i>⏳ Thinking...</i></div>`);

//         frappe.call({
//             method: "luggage_tracking.api.chatbot_reply",
//             args: {
//                 prompt: question
//             },
//             callback: function(r) {
//                 // Remove the "Thinking..." text (last div)
//                 $('#chat_output div:last').remove();

//                 if (r.message) {
//                     $('#chat_output').append(`<div><b>Bot:</b> ${r.message}</div>`);
//                 } else {
//                     $('#chat_output').append(`<div><b>Bot:</b> ❌ No response received.</div>`);
//                 }

//                 $('#user_input').val(""); // clear input
//                 // Scroll to bottom
//                 $('#chat_output').scrollTop($('#chat_output')[0].scrollHeight);
//             }
//         });
//     });

//     // Clear button handler
//     $('#clear_btn').on('click', function() {
//         $('#chat_output').empty();
//         $('#user_input').val('');
//     });
// };
