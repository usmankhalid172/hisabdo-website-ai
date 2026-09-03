# HisabDo AI Help & Support System

A Flask REST API prototype for AI-powered, context-aware user assistance for HisabDo.

The system combines a verified local FAQ knowledge base with a lightweight local AI model and existing support modules to provide controlled and reliable user assistance.

## Features

- Context-aware assistance
- AI Assistant endpoint
- Verified FAQ / knowledge-base support
- Local AI model fallback
- Feature guidance
- Step-by-step help
- Error assistance
- Help article suggestions
- Confidence evaluation
- Response validation
- Related questions
- Support automation
- Human escalation
- Web UI
- Input validation
- Query length validation
- Rate limiting
- CORS support
- Standardized JSON responses
- HTTP 404 / 405 error handling
- API health check

## AI Assistant Flow

The main AI Assistant follows a controlled response flow:

User Query
    |
    v
Input Validation
    |
    v
Verified FAQ Search
    |
    +---- Match ----> Verified FAQ Response
    |
    +---- No Match
            |
            v
       Local AI Model
            |
            v
      Response Validation
            |
            v
       Final Response

The verified FAQ knowledge base is checked first so that known support questions can be answered using controlled information.


## Installation

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Copy `.env.example` to `.env` if custom local configuration is required.

## Run

Start the Flask application:

```bash
python app.py
```

The API will run locally at:

```text
http://127.0.0.1:5000
```

## API Endpoints

### API Health Check

```text
GET /health
```

Example:

```text
http://127.0.0.1:5000/health
```

### AI Assistant

```text
POST /ai/assistant
```

Request:

```json
{
  "query": "How can I add an expense?"
}
```

The assistant first searches the verified FAQ knowledge base. If no matching FAQ is found, the local AI model is used.

### Context-Aware Help

```text
POST /ai/help/context
```

### Feature Guidance

```text
POST /ai/help/feature
```

### Step-by-Step Help

```text
POST /ai/help/steps
```

### Error Assistance

```text
POST /ai/help/error
```

### Help Articles

```text
POST /ai/help/articles
```

### Support Automation

```text
POST /ai/help/automate
```

### Human Escalation

```text
POST /ai/help/escalate
```

### FAQ Support

```text
POST /ai/help/faq
```

The FAQ endpoint also provides related questions when a matching FAQ is found.

## Example FAQ Request

```text
POST /ai/help/faq
```

Request:

```json
{
  "query": "How can I add an expense?"
}
```

## Validation

The API validates incoming requests before processing them.

For example:

* Request body must be provided.
* Query must not be empty.
* Query length is limited to 500 characters.
* Invalid AI responses are rejected.
* Empty AI answers are rejected.

Example validation response:

```json
{
  "success": false,
  "error": "Query is required."
}
```

## Rate Limiting

The API uses Flask-Limiter for basic request protection.

Default limit:

```text
100 requests per minute
```

The FAQ endpoint has a stricter limit:

```text
20 requests per minute
```

If the rate limit is exceeded, the API returns HTTP `429`.

## Error Handling

The API provides standardized error responses for common HTTP errors.

### 404

```json
{
  "status": "error",
  "message": "API endpoint not found.",
  "data": null
}
```

### 405

```json
{
  "status": "error",
  "message": "HTTP method not allowed.",
  "data": null
}
```

### 429

```json
{
  "status": "error",
  "message": "Too many requests. Please try again later.",
  "data": null
}
```

## Testing

The API can be tested using:

* Thunder Client
* Postman
* curl
* Browser for GET endpoints

Recommended tests include:

1. Health check
2. AI Assistant with a known FAQ question
3. AI Assistant with an unknown question
4. Empty query validation
5. Long query validation
6. FAQ endpoint
7. Context-aware help
8. Feature guidance
9. Step-by-step help
10. Error assistance
11. Help articles
12. Support automation
13. Human escalation
14. 404 endpoint
15. 405 HTTP method
16. Rate limiting

## Security and Reliability

The prototype includes:

* Input validation
* Query length restrictions
* Rate limiting
* CORS configuration
* Controlled FAQ knowledge base
* Response validation
* Standardized error handling

These controls help keep the prototype lightweight and reduce unnecessary or uncontrolled AI responses.

## Prototype Limitations

This project is a prototype using a local JSON knowledge base and lightweight local AI components.

For production deployment, the system should additionally implement:

* Authentication and authorization
* HTTPS
* Restricted CORS
* Persistent support tickets
* Production monitoring and logging
* Production-grade semantic retrieval / RAG
* Stronger response evaluation
* Database-backed knowledge management
* Production AI model integration

## Development Status

The current POC demonstrates a controlled AI help and support workflow with multiple support capabilities, FAQ-based knowledge retrieval, local AI fallback, validation, rate limiting, and standardized API responses.

## License

This project is intended for educational and internship POC purposes.