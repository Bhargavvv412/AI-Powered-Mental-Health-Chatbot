const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");
const themeToggle = document.getElementById("theme-toggle");

const API_URL = "http://127.0.0.1:8000/chat";
const SESSION_ID = "frontend_user_001";

// Add message bubble
function addMessage(message, sender = "bot") {
    const msgDiv = document.createElement("div");
    msgDiv.classList.add(sender === "user" ? "user-msg" : "bot-msg");
    msgDiv.textContent = message;
    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Send message
async function sendMessage() {
    const query = userInput.value.trim();
    if (!query) return;

    addMessage(query, "user");
    userInput.value = "";

    try {
        const res = await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ session_id: SESSION_ID, query }),
        });

        const data = await res.json();
        addMessage(data.response || "🤔 Hmm, I’m not sure. Try rephrasing!");
    } catch (error) {
        addMessage("⚠️ Unable to connect to the server. Please check backend.", "bot");
    }
}

// Events
sendBtn.addEventListener("click", sendMessage);
userInput.addEventListener("keypress", (e) => e.key === "Enter" && sendMessage());

// === THEME TOGGLE ===
themeToggle.addEventListener("click", () => {
    document.body.classList.toggle("dark");
    const icon = themeToggle.textContent.trim();
    themeToggle.textContent = icon === "🌙" ? "☀️" : "🌙";
});
