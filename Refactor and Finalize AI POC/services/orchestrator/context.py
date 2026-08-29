"""
Simple session context for the HisabDo POC.

This is intentionally lightweight and stores only the latest
conversation context.
"""


class ConversationContext:
    def __init__(self):
        self.last_query = None
        self.last_intent = None
        self.last_category = None
        self.last_answer = None

    def update(
        self,
        query: str,
        intent: str,
        category: str = None,
        answer: str = None,
    ):
        self.last_query = query
        self.last_intent = intent
        self.last_category = category
        self.last_answer = answer

    def get_context(self):
        return {
            "last_query": self.last_query,
            "last_intent": self.last_intent,
            "last_category": self.last_category,
            "last_answer": self.last_answer,
        }

    def has_context(self) -> bool:
        return self.last_query is not None

    def enrich_follow_up(self, query: str) -> str:
        """
        Add previous context to a short follow-up query.
        """
        if not self.has_context():
            return query

        text = query.strip().lower()

        follow_up_phrases = [
            "what information",
            "what details",
            "how",
            "what about",
            "and then",
            "what next",
            "phir",
            "aur",
            "kya chahiye",
        ]

        if any(phrase in text for phrase in follow_up_phrases):
            return f"{query} {self.last_category or ''} {self.last_intent or ''}"

        return query