const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");

const API_URL = "http://127.0.0.1:8000/chat"; // Your FastAPI endpoint
const SESSION_ID = "frontend_user_001";

// Add message to chat box
function addMessage(message, sender = "bot") {
    const msgDiv = document.createElement("div");
    msgDiv.classList.add(sender === "user" ? "user-msg" : "bot-msg");
    msgDiv.textContent = message;
    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Send message to FastAPI backend
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
        addMessage(data.response || "🤔 Sorry, I didn’t quite catch that.");
    } catch (error) {
        addMessage("⚠️ Error connecting to server. Please check if backend is running.");
        console.error(error);
    }
}

// Event listeners
sendBtn.addEventListener("click", sendMessage);
userInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") sendMessage();
});
