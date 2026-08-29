# HisabDo AI Help & Support API

A simple Flask-based prototype for context-aware user assistance and systematic testing.

## Project Structure

- `app.py` — Flask API
- `requirements.txt` — Python dependencies
- `tests/test_user_queries.md` — documented testing dataset with 52 test cases

## Setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

## API Endpoints

### GET /
Checks API status.

### POST /ai/help/context

Example request:

```json
{
  "query": "What is HisabDo?"
}
```

## Testing

Use Postman or THUNDER client to send requests to:

`http://127.0.0.1:5000/ai/help/context`

Record the actual response, status, issues, and improvements in `tests/test_user_queries.md`.
