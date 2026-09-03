from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


# Controlled and verified training data
TRAINING_DATA = [
    ("how can i add an expense", "expense"),
    ("how do i add an expense", "expense"),
    ("i want to record an expense", "expense"),
    ("how can i record spending", "expense"),

    ("how can i manage my budget", "budget"),
    ("how do i create a budget", "budget"),
    ("tell me about budget", "budget"),
    ("how can i track my budget", "budget"),

    ("i need help", "help"),
    ("how can you help me", "help"),
    ("what can you do", "help"),
    ("i need assistance", "help"),
]


texts = [item[0] for item in TRAINING_DATA]
labels = [item[1] for item in TRAINING_DATA]


# Convert text into numerical features
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(texts)


# Train lightweight classification model
model = LogisticRegression(max_iter=1000)

model.fit(X, labels)


def generate_ai_response(query):
    """
    Generate a response using the trained local AI model.
    """

    query = query.strip()

    if not query:
        return {
            "success": False,
            "answer": None,
            "confidence": 0.0,
            "error": "Query cannot be empty."
        }

    # Convert user query into TF-IDF features
    query_vector = vectorizer.transform([query])

    # Predict category
    prediction = model.predict(query_vector)[0]

    # Get confidence
    probabilities = model.predict_proba(query_vector)[0]
    confidence = float(max(probabilities))

    responses = {
        "expense": (
            "You can add an expense by opening the expense section, "
            "entering the required details, and saving the record."
        ),

        "budget": (
            "You can use the budget section to create and monitor "
            "your planned spending."
        ),

        "help": (
            "I can help you with HisabDo expenses, budgets, "
            "and other supported features."
        )
    }

    answer = responses.get(
        prediction,
        "I could not find a verified answer for this question."
    )

    return {
        "success": True,
        "query": query,
        "intent": prediction,
        "confidence": round(confidence, 2),
        "answer": answer
    }