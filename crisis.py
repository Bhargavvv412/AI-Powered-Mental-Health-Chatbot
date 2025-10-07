from typing import List

# Crisis-related keywords to detect distress or self-harm intent
CRISIS_KEYWORDS: List[str] = [
    "suicidal",
    "suicide",
    "kill myself",
    "want to die",
    "hopeless",
    "worthless",
    "can't go on",
    "cannot go on",
    "give up",
    "ending it all",
    "no reason to live",
    "end my life",
    "i want to disappear",
    "self harm",
    "cut myself",
]

# Safety message the bot will respond with if crisis keywords are detected
SAFETY_MESSAGE = (
    "💛 It sounds like you’re going through something really difficult right now. "
    "You are **not alone**, and your life matters deeply.\n\n"
    "If you’re in immediate danger or thinking about ending your life, please reach out for help right away:\n\n"
    "**📞 India:** AASRA Helpline — 91-9820466726 or call 1800 599 0019\n"
    "**📞 USA:** National Suicide and Crisis Lifeline — 988 (24/7)\n"
    "**📞 UK:** Samaritans — 116 123 (24/7)\n\n"
    "You deserve care, support, and understanding. ❤️\n"
    "Please consider talking to a trusted friend, family member, or a mental health professional.\n\n"
    "**You matter.** The world is better with you in it. 🌻"
)

def contains_crisis_keywords(text:str) -> bool:
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in CRISIS_KEYWORDS)