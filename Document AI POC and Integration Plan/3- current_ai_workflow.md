# 3. Current AI Workflow

## 3.1 Overview

The current AI workflow describes how a user request moves through the HisabDo AI Help & Support system.

The system follows a modular workflow in which the incoming request is validated, processed, directed to the appropriate support functionality, and converted into a response.

## 3.2 Workflow

The current workflow can be represented as:

```text
User
  ↓
User Query
  ↓
HisabDo Frontend
  ↓
Flask REST API
  ↓
Request Validation
  ↓
Input Processing
  ↓
Intent / Request Identification
  ↓
Appropriate AI Support Service
  ↓
Response Generation
  ↓
JSON Response
  ↓
Frontend
  ↓
User
```

## 3.3 Step-by-Step Process

### Step 1: User Query

The process starts when a user submits a question or support request.

Example:

```text
"How can I add a new expense?"
```

### Step 2: API Request

The frontend sends the user's request to the Flask REST API using an HTTP request.

The request data is generally provided in JSON format.

Example:

```json
{
    "query": "How can I add a new expense?"
}
```

### Step 3: Request Validation

The API checks whether the request contains valid data.

If the required data is missing, the API returns an appropriate error response instead of processing an invalid request.

### Step 4: Input Processing

The received information is processed so that it can be used by the relevant support service.

The system can use user-provided context, query information, or structured expense data depending on the requested functionality.

### Step 5: Request / Intent Identification

The system determines what type of assistance is required.

Possible request types include:

* Feature guidance
* Step-by-step help
* Error assistance
* FAQ or help article suggestion
* Context-aware assistance
* Personalized recommendation
* Human escalation

### Step 6: Support Service

After identifying the required functionality, the request is passed to the relevant support module.

The current project follows a modular structure with separate services for different support functions.

Examples include:

```text
feature_guidance
step_help
error_assistance
help_articles
support_automation
escalation
context_support
recommendations
```

### Step 7: Response Generation

The selected service processes the request and generates a suitable support response.

The response should be:

* Relevant
* Clear
* Concise
* User-friendly
* Based on available information

### Step 8: API Response

The Flask API returns the result to the frontend in JSON format.

Example:

```json
{
    "status": "success",
    "response": "Open the Expenses section and select Add Expense."
}
```

### Step 9: User Receives Assistance

The frontend displays the generated response to the user.

The user can then follow the provided instructions or submit another question.

## 3.4 Example Workflow

For example, if a user asks:

```text
"How do I add an expense?"
```

The workflow is:

```text
User Query
    ↓
Flask API
    ↓
Validate Request
    ↓
Identify Feature Guidance Request
    ↓
feature_guidance Service
    ↓
Generate Instructions
    ↓
JSON Response
    ↓
Frontend
    ↓
User
```

## 3.5 Error Handling

If the request is missing required information or cannot be processed, the system should return a clear error response.

The API should avoid exposing internal implementation details or technical errors directly to the end user.

## 3.6 Workflow Objective

The objective of this workflow is to create a structured and modular AI support process that can be extended with additional AI capabilities, knowledge sources, security controls, and future RAG integration.
