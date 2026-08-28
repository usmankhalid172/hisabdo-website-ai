# hisabdo-website-ai
# HisabDo — AI User Engagement Engine

Flask REST API implementing 14 rule-based AI engagement features for
HisabDo shopkeepers, plus an aggregating dashboard endpoint. Turns
everyday shop data (expenses, sales, customers, payments) into
recommendations, alerts, scores, and a personalized dashboard.

Full technical documentation — architecture, API reference, AI logic,
security notes, test results, and a known-issue writeup — is available
in `HisabDo_AI_Engagement_Engine_Documentation.docx`.

## Quick start

```bash
pip install -r requirements.txt pandas
python app.py
curl http://127.0.0.1:5000/
# {"status": "success", "message": "HisabDo AI API is running"}
```

## Endpoints

| Endpoint | Feature |
|---|---|
| `POST /ai/personalized-recommendation` | Personalized Recommendations |
| `POST /ai/smart-financial-alerts` | Smart Financial Alerts |
| `POST /ai/daily-business-brief` | Daily Business Brief |
| `POST /ai/payment-reminders` | Predictive Payment Reminders |
| `POST /ai/customer-followup` | AI Customer Follow-Up Suggestions |
| `POST /ai/context-suggestion` | Context-Aware AI Suggestions |
| `POST /ai/feature-discovery` | Smart Feature Discovery |
| `POST /ai/financial-goal` | Financial Goal Tracking |
| `POST /ai/action-plan` | Personalized Action Plans |
| `POST /ai/business-health` | Business Health Score |
| `POST /ai/predictive-expense-alert` | Predictive Expense Alerts |
| `POST /ai/customer-risk` | Customer Risk Signals |
| `POST /ai/notification-priority` | Notification Prioritization |
| `POST /ai/monthly-insights` | Monthly Insights |
| `POST /ai/dashboard` | Personalized AI Dashboard (aggregator) |

See `documentation.md` for per-feature purpose/input/processing notes,
or the technical documentation for full request/response examples.

## Known issue

`/ai/personalized-recommendation` and `/ai/smart-financial-alerts`
return HTTP 500 (`Object of type int64 is not JSON serializable`) if
`amount` values in the `expenses` array are sent as JSON integers
(e.g. `15000`). Send them as decimals (`15000.0`) until this is fixed.
Root cause: pandas infers an `int64` dtype for the `amount` column when
every value is a JSON integer, and `round()` on an `int64` returns a
`numpy.int64`, which Flask's default JSON encoder cannot serialize.
Fix: cast summary values with `float(...)` before returning them, or
`.astype(float)` the `amount` column right after `pd.to_numeric()`.
Details in the technical documentation, Section 11.2.

## Architecture

```
HisabDo Client (mobile/web)
        │  HTTPS POST /ai/*  (JSON)
        ▼
Flask REST API (app.py — 15 routes)
        │  route dispatch
        ▼
Service Layer (services/*.py — 14 modules)
        │  pandas + hand-tuned thresholds
        ▼
JSON Response (status, metrics, ai_insight)
```

No database, no persistence — every request is stateless. History-
dependent features (Customer Follow-Up, Payment Reminders) require the
caller to send full history with each request.

## Requirements

See `requirements.txt` for pinned versions (Flask, Werkzeug, Jinja2).
`pandas` is required by `app.py` and most `services/*.py` modules but
is not currently pinned in `requirements.txt` — install it separately.

## Status

Prototype / capstone deliverable. Not production-ready: no
authentication, no rate limiting, debug mode enabled, and no automated
test suite ship with the module. See the technical documentation,
Sections 9, 12, and 13, before any real deployment.
