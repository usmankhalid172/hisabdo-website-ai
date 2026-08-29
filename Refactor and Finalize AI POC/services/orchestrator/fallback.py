"""
Safe fallback responses for the HisabDo AI POC.
"""

FALLBACK_MESSAGES = {
    "english": {
        "unknown": (
            "I couldn't find a verified HisabDo answer for that question."
        ),
        "ambiguous": (
            "Could you clarify what you would like to do? "
            "For example, you can ask about customers, expenses, "
            "transactions, accounts, or other HisabDo features."
        ),
        "unsupported": (
            "I don't have verified information about that HisabDo feature yet."
        ),
        "financial": (
            "I don't have verified financial data to provide that number."
        ),
        "low_confidence": (
            "I couldn't find enough verified information to answer that reliably."
        ),
        "greeting": (
            "Hello! I'm the HisabDo assistant. Ask me about expenses, "
            "customers, transactions, accounts, or any other HisabDo feature."
        ),
        "thanks": (
            "You're welcome! Let me know if you have any other questions "
            "about HisabDo."
        ),
    },

    "roman_urdu": {
        "unknown": (
            "Mujhe is sawal ka verified HisabDo jawab nahi mila."
        ),
        "ambiguous": (
            "Kya aap thora wazeh kar sakte hain ke aap kya karna chahte hain? "
            "Aap customer, expense, transaction ya account ke bare mein pooch sakte hain."
        ),
        "unsupported": (
            "Mere paas is HisabDo feature ke bare mein verified information nahi hai."
        ),
        "financial": (
            "Mere paas yeh financial number provide karne ke liye verified data nahi hai."
        ),
        "low_confidence": (
            "Mujhe reliable jawab dene ke liye kafi verified information nahi mili."
        ),
        "greeting": (
            "Assalam-o-Alaikum! Main HisabDo assistant hoon. Aap mujh se "
            "expenses, customers, transactions ya accounts ke bare mein pooch sakte hain."
        ),
        "thanks": (
            "Khushamdeed! Agar koi aur sawal ho to zaroor poochein."
        ),
    },

    "urdu": {
        "unknown": (
            "مجھے اس سوال کا تصدیق شدہ HisabDo جواب نہیں ملا۔"
        ),
        "ambiguous": (
            "براہ کرم واضح کریں کہ آپ کیا کرنا چاہتے ہیں۔"
        ),
        "unsupported": (
            "میرے پاس اس HisabDo فیچر کے بارے میں تصدیق شدہ معلومات موجود نہیں ہیں۔"
        ),
        "financial": (
            "میرے پاس یہ مالی عدد فراہم کرنے کے لیے تصدیق شدہ ڈیٹا موجود نہیں ہے۔"
        ),
        "low_confidence": (
            "قابل اعتماد جواب دینے کے لیے کافی تصدیق شدہ معلومات نہیں ملیں۔"
        ),
        "greeting": (
            "السلام علیکم! میں HisabDo اسسٹنٹ ہوں۔ آپ مجھ سے اخراجات، "
            "کسٹمرز، لین دین یا اکاؤنٹس کے بارے میں پوچھ سکتے ہیں۔"
        ),
        "thanks": (
            "خوش آمدید! اگر کوئی اور سوال ہو تو ضرور پوچھیں۔"
        ),
    },
}


def get_fallback(language: str, fallback_type: str = "unknown") -> str:
    language_messages = FALLBACK_MESSAGES.get(
        language,
        FALLBACK_MESSAGES["english"],
    )

    return language_messages.get(
        fallback_type,
        language_messages["unknown"],
    )