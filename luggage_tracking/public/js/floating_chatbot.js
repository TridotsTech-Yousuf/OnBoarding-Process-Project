frappe.after_ajax(() => {
    // Inject floating button
    const btn = document.createElement('div');
    btn.innerHTML = '💬';
    btn.id = 'chatbot-float-btn';
    Object.assign(btn.style, {
        position: 'fixed',
        bottom: '30px',
        right: '30px',
        background: '#007bff',
        color: 'white',
        borderRadius: '50%',
        width: '60px',
        height: '60px',
        fontSize: '30px',
        textAlign: 'center',
        lineHeight: '60px',
        cursor: 'pointer',
        zIndex: 9999
    });
    document.body.appendChild(btn);

    // Chat popup window
    const popup = document.createElement('div');
    popup.id = 'chatbot-popup';
    popup.style = `
        display: none;
        position: fixed;
        bottom: 100px;
        right: 30px;
        width: 600px;
        height: 400px;
        background: white;
        border: 1px solid #ccc;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0,0,0,0.2);
        z-index: 9999;
        padding: 10px;
        overflow-y: auto;
    `;
    popup.innerHTML = `
        <div id="chat_output" style="height: 80%; overflow-y: auto;">
            <button id="Create Doctype" class="btn btn-sm btn-secondary">Create Doctype</button>
        </div>
        <div style="display:flex; margin-top:10px;">
            <input id="user_input" type="text" placeholder="Ask something..." style="flex:1;" />
            <button id="send_btn" class="btn btn-sm btn-primary" style="margin-left:5px;">Send</button>
        </div>
    `;
    document.body.appendChild(popup);

    // Toggle popup
    btn.onclick = () => {
        popup.style.display = popup.style.display === 'none' ? 'block' : 'none';
    };

    // Create Doctype button handler
    document.addEventListener('click', function (e) {
        if (e.target && e.target.id === 'Create Doctype') {
            const chatOutput = document.getElementById('chat_output');
            chatOutput.innerHTML += `<div><b>You:</b> Create Doctype</div>`;
            chatOutput.innerHTML += `<div><i>⏳ Thinking...</i></div>`;

            frappe.call({
                method: "luggage_tracking.api.chatbot_reply",
                args: { prompt: "create doctype" },
                callback: function (r) {
                    chatOutput.lastChild.remove();
                    chatOutput.innerHTML += `<div><b>Bot:</b> ${r.message || "❌ No response."}</div>`;
                    chatOutput.scrollTop = chatOutput.scrollHeight;
                }
            });
        }
    });

    // Send button handler
    document.addEventListener('click', function (e) {
        if (e.target && e.target.id === 'send_btn') {
            const question = document.getElementById('user_input').value.trim();
            if (!question) return;

            const chatOutput = document.getElementById('chat_output');
            chatOutput.innerHTML += `<div><b>You:</b> ${question}</div>`;
            chatOutput.innerHTML += `<div><i>⏳ Thinking...</i></div>`;
            document.getElementById('user_input').value = '';

            frappe.call({
                method: "luggage_tracking.api.chatbot_reply",
                args: { prompt: question },
                callback: function (r) {
                    chatOutput.lastChild.remove();
                    chatOutput.innerHTML += `<div><b>Bot:</b> ${r.message || "❌ No response."}</div>`;
                    chatOutput.scrollTop = chatOutput.scrollHeight;
                    document.getElementById('user_input').focus();
                }
            });
        }
    });
});
