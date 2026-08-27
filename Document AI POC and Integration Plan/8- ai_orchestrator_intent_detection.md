# 8. AI Orchestrator / Intent Detection

## 8.1 Overview

The AI Orchestrator is the logical component responsible for managing the flow of a user's request through the AI Help & Support system.

Its main responsibility is to identify what type of assistance the user needs and route the request to the appropriate support service.

## 8.2 What is Intent?

Intent means the actual purpose behind a user's question.

For example:

```text
User:
"How can I add a new expense?"

Intent:
Feature Guidance
```

Another example:

```text
User:
"My expense is not being saved."

Intent:
Error Assistance
```

The wording of the questions is different, but the system focuses on understanding what the user wants.

## 8.3 Main Intent Categories

The current support system can work with the following intent categories:

| Intent             | Purpose                                   |
| ------------------ | ----------------------------------------- |
| Feature Guidance   | Explain how to use a feature              |
| Step Help          | Provide step-by-step instructions         |
| Error Assistance   | Help troubleshoot a problem               |
| FAQ                | Answer common questions                   |
| Help Article       | Suggest relevant help content             |
| Context Help       | Provide context-aware assistance          |
| Recommendation     | Provide personalized recommendations      |
| Support Automation | Handle routine support requests           |
| Escalation         | Transfer difficult cases to human support |

## 8.4 Intent Detection Flow

The basic process is:

```text
User Query
    ↓
Input Validation
    ↓
Query Processing
    ↓
Intent Identification
    ↓
Select Appropriate Service
    ↓
Generate Response
    ↓
Return Response
```

## 8.5 Example 1 — Feature Guidance

```text
User:
How do I add an expense?

Intent:
Feature Guidance

Service:
feature_guidance
```

The request is routed to the feature guidance functionality.

## 8.6 Example 2 — Error Assistance

```text
User:
I cannot save my expense.

Intent:
Error Assistance

Service:
error_assistance
```

The system can provide troubleshooting guidance or request additional information.

## 8.7 Example 3 — Step-by-Step Help

```text
User:
Show me the steps to manage my expenses.

Intent:
Step Help

Service:
step_help
```

The system provides instructions in a sequential format.

## 8.8 Example 4 — Personalized Recommendation

If the request contains structured expense information, the system can route the request to the recommendation functionality.

Example:

```json
{
    "expenses": [
        {
            "amount": 2500,
            "category": "Food"
        }
    ]
}
```

The recommendation service processes the available expense information.

## 8.9 Ambiguous Intent

Sometimes a user query may not clearly indicate the required support type.

Example:

```text
User:
It is not working.
```

The system should not assume the problem.

Instead, it should request clarification, such as:

```text
Which feature is not working, and what error message are you seeing?
```

## 8.10 Unknown Intent

If the system cannot identify a suitable intent, it should use a safe fallback.

Possible actions include:

* Ask the user to clarify the question.
* Provide general supported guidance.
* Suggest relevant help content.
* Escalate to human support when necessary.

## 8.11 Role of the Orchestrator

The orchestrator helps keep the support architecture organized by separating request routing from individual support services.

This modular approach makes it easier to add or update capabilities without redesigning the entire system.

## 8.12 Expected Outcome

The AI Orchestrator should ensure that each user request is directed to the most appropriate support functionality.

This improves response relevance, maintainability, scalability, and overall user experience.
