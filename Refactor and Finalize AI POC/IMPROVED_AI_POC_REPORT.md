# Improved AI POC Report

**Owner:** LY

## 1. Objective

The objective of this POC is to improve the quality, consistency, relevance,
and safety of AI responses for the HisabDo website.

## 2. Improvements

The POC introduces:

- Input validation
- Language detection
- Intent detection
- Query normalization
- Verified FAQ retrieval
- Confidence-based handling
- Response quality validation
- Safe fallback responses
- Basic conversation context
- Related question support
- Unknown-query handling
- Unclear-query handling

## 3. Intent Categories

The POC currently supports:

- Product information
- Feature
- How-to
- FAQ
- Support
- Unknown

## 4. Language Handling

The POC detects:

- English
- Urdu
- Roman Urdu

Language detection is used to select appropriate fallback responses.

## 5. Verified Content

The FAQ knowledge base uses a `verified` field.

Only content marked as verified is eligible for direct AI responses.

Each entry also contains a source field.

## 6. Response Quality

Responses are checked for:

- Verification
- Relevance
- Clarity
- Confidence
- Generic unnecessary content

## 7. Fallback Handling

The POC uses different fallback responses for:

- Unknown queries
- Ambiguous queries
- Low-confidence queries
- Unsupported information
- Unverified information

## 8. Context

The POC stores basic session information:

- Previous query
- Previous intent
- Previous category
- Previous answer

This allows simple follow-up questions to use previous context.

## 9. Hallucination Prevention

The system does not intentionally generate unsupported product information.

If verified content cannot be found, the system returns a safe fallback.

Financial numerical information is not accepted from unverified responses.

## 10. Testing

Testing includes:

- Product queries
- Feature queries
- FAQ queries
- Help/support queries
- Unknown queries
- Unclear queries
- English
- Urdu
- Roman Urdu
- Context follow-ups
- Fallback responses
- Response validation

## 11. Current Capabilities

The POC can:

- Identify basic user intent
- Search controlled FAQ content
- Reject unverified content
- Detect English, Urdu and Roman Urdu
- Handle unknown questions safely
- Handle ambiguous questions
- Perform basic response-quality checks
- Maintain basic conversation context

## 12. Technical Limitations

The current implementation is a POC and has several limitations:

- Intent detection is rule-based.
- Retrieval uses lightweight text similarity.
- The knowledge base is limited.
- Urdu/Roman Urdu answer coverage depends on verified content.
- Context is basic and session-level.
- No advanced semantic/vector retrieval is currently implemented.
- No production-grade conversational memory is implemented.
- No real-time financial data integration is implemented.

## 13. Future Requirements

The next version can include:

1. Semantic/vector retrieval
2. Larger verified knowledge base
3. Better intent classification
4. Better Roman Urdu normalization
5. Expanded Urdu responses
6. Advanced conversation memory
7. Knowledge-base versioning
8. Source citations
9. Automated response evaluation
10. User feedback collection

## 14. Conclusion

The improved POC provides a more controlled and reliable AI support workflow.

Instead of returning an answer whenever a textual match is found, the system now
considers intent, verification, confidence, response quality and fallback handling.

This reduces unsupported answers and improves the consistency and safety of
HisabDo AI responses.