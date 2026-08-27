# 4. Chatbot Capabilities

## 4.1 Overview

The HisabDo AI Help & Support chatbot is designed to assist users with common application-related questions and support requests.

The chatbot focuses on providing relevant guidance, troubleshooting assistance, FAQs, contextual help, and personalized support.

## 4.2 Supported Query Types

The chatbot can support the following major query types:

### 1. Feature Guidance

The chatbot can explain how users can use different HisabDo features.

Example:

```text
User:
"How can I add an expense?"
```

Expected assistance:

```text
The chatbot provides the basic steps required to add an expense.
```

### 2. Step-by-Step Help

The chatbot can provide instructions in a simple sequence of steps.

Example:

```text
User:
"Tell me step by step how to manage my expenses."
```

The response should present the process in an easy-to-follow format.

### 3. Error Assistance

The chatbot can help users understand common application errors.

Example:

```text
User:
"I am getting an error while adding an expense."
```

The system can ask for relevant information and provide troubleshooting guidance.

### 4. FAQ Handling

The chatbot can answer frequently asked questions using approved FAQ or knowledge-base information.

Example:

```text
User:
"What is HisabDo used for?"
```

The chatbot should provide information that is available in the approved knowledge source.

### 5. Help Article Suggestions

The system can suggest relevant help articles when additional information is required.

Example:

```text
User:
"How can I manage my monthly expenses?"
```

The chatbot can identify relevant help content for the user.

### 6. Context-Aware Assistance

The chatbot can use available user context to provide more relevant assistance.

For example, if the request contains information about a specific feature or problem, the response can be tailored to that context.

### 7. Personalized Recommendations

The system can process structured expense information and generate personalized recommendations.

For example, the system can analyze expense data containing:

```text
amount
category
```

and provide recommendations based on the available information.

### 8. Support Automation

Common support requests can be processed automatically without requiring immediate human intervention.

This can reduce the workload on manual support teams for routine questions.

### 9. Human Escalation

If the chatbot cannot confidently handle a request, the system can use an escalation mechanism so that the issue can be transferred to human support.

## 4.3 Query Categories

The supported capabilities can be summarized as:

| Query Type                  | Purpose                         |
| --------------------------- | ------------------------------- |
| Feature Guidance            | Explain application features    |
| Step-by-Step Help           | Provide instructions            |
| Error Assistance            | Help troubleshoot common issues |
| FAQ                         | Answer common questions         |
| Help Articles               | Suggest relevant information    |
| Context-Aware Help          | Use available context           |
| Personalized Recommendation | Analyze available expense data  |
| Support Automation          | Handle routine requests         |
| Human Escalation            | Transfer difficult cases        |

## 4.4 Out-of-Scope Queries

The chatbot should not provide unsupported information about HisabDo.

For example, if the required information is not available in the approved knowledge sources, the system should not invent an answer.

Instead, it should provide a safe fallback response or recommend contacting human support.

## 4.5 Capability Objective

The objective is to provide users with a single AI support interface that can handle common questions, guide users through application features, assist with errors, and provide personalized support while maintaining accuracy and reliability.
