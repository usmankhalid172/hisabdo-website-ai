# 11. Anti-Hallucination & AI Safety Rules

## 11.1 Overview

AI hallucination occurs when an AI system generates information that is incorrect, unsupported, or not available in its trusted information sources.

For the HisabDo AI Help & Support system, preventing unsupported answers is important because users may rely on the chatbot for application-related guidance.

## 11.2 Main Objective

The objective is to ensure that the AI provides information based on trusted and available sources instead of inventing application features, policies, procedures, or other unsupported information.

## 11.3 Core Rules

### Rule 1 — Do Not Guess

If the system does not have enough reliable information to answer a question, it should not guess.

Instead, it should provide a safe fallback response.

Example:

```text
I don't have enough verified information to answer that accurately. Please provide more details or contact support.
```

### Rule 2 — Use Trusted Information

Responses about HisabDo should be based on approved sources such as:

* Official FAQs
* Help articles
* Application documentation
* Verified system information
* Approved knowledge-base content

### Rule 3 — Do Not Invent Features

The chatbot must not claim that HisabDo has a feature when that feature has not been verified.

For example, the AI should not say:

```text
"HisabDo has an automatic feature X."
```

unless the feature exists in an approved source.

### Rule 4 — Handle Uncertainty

If the system is uncertain about the user's request, it should ask a clarification question rather than making assumptions.

Example:

```text
Could you tell me which HisabDo feature you are having trouble with?
```

### Rule 5 — Use Context Carefully

User-provided context should be used to improve relevance, but the system should not treat unsupported user statements as verified facts.

### Rule 6 — Safe Fallback

When no reliable answer is available, the system should:

1. Avoid generating unsupported information.
2. Inform the user that more information is required.
3. Ask for clarification when appropriate.
4. Suggest relevant help content if available.
5. Escalate to human support when necessary.

## 11.4 Confidence-Based Handling

Future versions can use confidence thresholds when selecting or generating responses.

A simplified approach can be:

```text
High Confidence
      ↓
Provide Answer

Low Confidence
      ↓
Ask Clarification / Fallback

Very Low Confidence
      ↓
Human Escalation
```

The exact threshold should be determined through testing rather than arbitrarily selected.

## 11.5 Response Validation

Before returning an AI-generated response, the system should ideally verify that:

* The response addresses the user's question.
* The information is supported by trusted sources.
* The response does not contain unsupported claims.
* Sensitive information is not unnecessarily exposed.
* The response follows the application's support rules.

## 11.6 Unsupported Query Example

User:

```text
Can HisabDo perform a feature that is not documented?
```

The chatbot should not invent an answer.

A safe response would be:

```text
I don't have verified information about that feature. Please check the available help documentation or contact support for confirmation.
```

## 11.7 Safety Boundaries

The AI support system should remain within its intended purpose.

It should primarily provide:

* HisabDo feature guidance
* Troubleshooting assistance
* FAQs
* Help information
* Context-aware support
* Approved recommendations

It should avoid presenting speculation as fact.

## 11.8 Monitoring and Improvement

Hallucination risks can be reduced over time by:

* Reviewing incorrect responses.
* Collecting user feedback.
* Updating the knowledge base.
* Improving retrieval quality.
* Testing ambiguous queries.
* Monitoring fallback rates.
* Adding RAG-based retrieval in future versions.
* Regularly reviewing AI prompts and response rules.

## 11.9 Expected Outcome

The anti-hallucination rules should make the AI Help & Support system more reliable by ensuring that unsupported information is not presented as fact.

When reliable information is unavailable, the system should prefer clarification, safe fallback, or human escalation instead of guessing.
