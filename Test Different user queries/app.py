from flask import Flask, request, jsonify

app = Flask(__name__)


# =========================
# HOME / API STATUS
# =========================
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "success",
        "message": "HisabDo AI Help & Support API is running"
    })


# =========================
# CONTEXT-AWARE AI HELP
# =========================
@app.route("/ai/help/context", methods=["POST"])
def context_help():

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "status": "error",
            "message": "Request body is required"
        }), 400

    query = data.get("query")

    if not query:
        return jsonify({
            "status": "error",
            "message": "Query is required"
        }), 400

    query = str(query).strip()

    if not query:
        return jsonify({
            "status": "error",
            "message": "Query cannot be empty"
        }), 400

    query_lower = query.lower()

    if "what is hisabdo" in query_lower:
        response = (
            "HisabDo is a financial management application "
            "that helps users manage and track their expenses."
        )

    elif "add an expense" in query_lower or "add expense" in query_lower:
        response = (
            "To add an expense, open the expense section in HisabDo, "
            "enter the expense details, select the appropriate category, "
            "and save the expense."
        )

    elif "reset my password" in query_lower or "reset password" in query_lower:
        response = (
            "To reset your password, use the password reset option "
            "on the login screen and follow the instructions."
        )

    elif "expense history" in query_lower:
        response = (
            "You can view your previous expenses from the expense "
            "history section of the application."
        )

    elif "hello" in query_lower or "hi" in query_lower:
        response = (
            "Hello! Welcome to HisabDo AI Help & Support. "
            "How can I help you?"
        )

    else:
        response = (
            "I can help you with HisabDo features, expenses, "
            "account questions, and general support. "
            "Please provide more details about your question."
        )

    return jsonify({
        "status": "success",
        "query": query,
        "response": response
    })


# =========================
# RUN APPLICATION
# =========================
if __name__ == "__main__":
    app.run(debug=True)
