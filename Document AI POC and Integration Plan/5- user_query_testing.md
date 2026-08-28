# 5. User Query Testing

## 5.1 Testing Objective

The objective of user query testing is to verify whether the AI Help & Support system can correctly process different types of user requests and provide relevant responses.

Testing focuses on common HisabDo support scenarios such as feature guidance, error assistance, FAQs, context-aware help, and personalized recommendations.

## 5.2 Test Scenarios

### Test Case 1 — Feature Guidance

**User Query:**

```text
How can I add a new expense?
```

**Expected Behavior:**

The system should identify the request as a feature-related query and provide clear instructions for adding an expense.

**Expected Result:**

Pass — relevant feature guidance is provided.

---

### Test Case 2 — Step-by-Step Help

**User Query:**

```text
Tell me step by step how to manage my expenses.
```

**Expected Behavior:**

The system should provide the instructions in a clear and sequential format.

**Expected Result:**

Pass — step-by-step guidance is provided.

---

### Test Case 3 — Error Assistance

**User Query:**

```text
I am getting an error while adding an expense.
```

**Expected Behavior:**

The system should identify this as an error-support request and provide troubleshooting guidance or request additional information when necessary.

**Expected Result:**

Pass — error assistance is triggered.

---

### Test Case 4 — FAQ

**User Query:**

```text
What is HisabDo?
```

**Expected Behavior:**

The system should provide a concise answer using approved application information.

**Expected Result:**

Pass — FAQ/general information response is provided.

---

### Test Case 5 — Context-Aware Assistance

**User Query:**

```text
I am trying to manage my expenses but I cannot find the required option.
```

**Expected Behavior:**

The system should use the available context to provide relevant assistance.

**Expected Result:**

Pass — contextual guidance is generated.

---

### Test Case 6 — Personalized Recommendation

**Input:**

```json
{
    "expenses": [
        {
            "amount": 2500,
            "category": "Food"
        },
        {
            "amount": 5000,
            "category": "Transport"
        }
    ]
}
```

**Expected Behavior:**

The system should validate the expense data and generate a recommendation based on the available information.

**Expected Result:**

Pass — personalized recommendation functionality is triggered.

---

### Test Case 7 — Missing Input

**User Query:**

```text
```

**Expected Behavior:**

The API should reject the empty or missing request and return an appropriate validation error.

**Expected Result:**

Pass — invalid input is handled safely.

---

### Test Case 8 — Unsupported Query

**User Query:**

```text
Tell me something that is not related to HisabDo.
```

**Expected Behavior:**

The system should avoid generating unsupported information and should use an appropriate fallback response.

**Expected Result:**

Pass — unsupported request is handled safely.

## 5.3 Testing Summary

| Test Case | Scenario                    | Expected Result          | Status |
| --------- | --------------------------- | ------------------------ | ------ |
| TC-01     | Feature Guidance            | Relevant instructions    | Pass   |
| TC-02     | Step-by-Step Help           | Sequential instructions  | Pass   |
| TC-03     | Error Assistance            | Troubleshooting guidance | Pass   |
| TC-04     | FAQ                         | Approved information     | Pass   |
| TC-05     | Context-Aware Help          | Contextual response      | Pass   |
| TC-06     | Personalized Recommendation | Recommendation           | Pass   |
| TC-07     | Missing Input               | Validation error         | Pass   |
| TC-08     | Unsupported Query           | Safe fallback            | Pass   |

## 5.4 Testing Conclusion

The test scenarios demonstrate the expected behavior of the current AI Help & Support POC across common user-support situations.

Further testing should be performed with real user queries, incorrect inputs, ambiguous questions, unexpected data, and edge cases before production deployment.
