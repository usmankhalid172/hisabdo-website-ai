# Deployment Architecture Report

## Current architecture

This repository contains multiple independent Flask prototypes and one root-level dependency file. The code is organized as a multi-feature AI prototype workspace rather than a single production app.

Current high-level layout:

- Root project folder
  - `requirements.txt` (minimal root dependency list)
  - `README.md`
  - `AI User Engagement Features/`
  - `AI-Powered Help/`
  - `Improve AI POC/`
  - Supporting documentation and design artifacts

The repository is not yet structured as a single deployable Flask service. The effective app layout is split across three independent Flask apps with overlapping features and import assumptions.

## Current Flask apps

### 1) AI User Engagement Features

Location:
- `AI User Engagement Features/app.py`

Purpose:
- AI engagement engine for business recommendations, alerts, insights, dashboarding, and financial analysis.

Main routes:
- `/`
- `/ai/personalized-recommendation`
- `/ai/smart-financial-alerts`
- `/ai/daily-business-brief`
- `/ai/payment-reminders`
- `/ai/customer-followup`
- `/ai/context-suggestion`
- `/ai/feature-discovery`
- `/ai/financial-goal`
- `/ai/action-plan`
- `/ai/business-health`
- `/ai/predictive-expense-alert`
- `/ai/customer-risk`
- `/ai/notification-priority`
- `/ai/monthly-insights`
- `/ai/dashboard`

Dependency structure:
- `services/*.py`
- `pandas`
- Flask only

### 2) AI-Powered Help

Location:
- `AI-Powered Help/app.py`

Purpose:
- Support and help assistant APIs for context-aware guidance, feature assistance, article suggestions, FAQ support, escalation, and automation.

Main routes:
- `/`
- `/ai/help/context`
- `/ai/help/feature`
- `/ai/help/steps`
- `/ai/help/error`
- `/ai/help/articles`
- `/ai/help/automate`
- `/ai/help/escalate`

Dependency structure:
- `services/support/*.py`
- JSON helper data file (`help_articles.json`)
- Flask only

### 3) Improve AI POC

Location:
- `Improve AI POC/app.py`

Purpose:
- More advanced help/support assistant with FAQ search, related-question retrieval, response-quality improvement, rate limiting, CORS, and UI route.

Main routes:
- `/`
- `/ui`
- `/health`
- `/api/info`
- `/ai/help/context`
- `/ai/help/feature`
- `/ai/help/steps`
- `/ai/help/error`
- `/ai/help/articles`
- `/ai/help/automate`
- `/ai/help/escalate`
- `/ai/help/faq`

Dependency structure:
- `config.py`
- `services/support/*.py`
- `faq.json`
- `index.html`
- Flask, Flask-Cors, Flask-Limiter

## Dependency map

### Root `requirements.txt`

The root dependency file currently includes only:

- Flask==3.1.3
- Werkzeug==3.1.8
- Jinja2==3.1.6
- MarkupSafe==3.0.3
- pandas
- gunicorn

This file is incomplete for the actual application set. It does not include the dependencies required by the enhanced support app:

- `Flask-Cors`
- `Flask-Limiter`

The app-specific subfolders each have their own requirements files, but the repository root is not yet a single deployable app.

## Import/module map

### AI User Engagement Features

Imports follow a pattern such as:

- `from services.financial_alerts import generate_smart_financial_alerts`
- `from services.daily_business_brief import generate_daily_business_brief`
- `from services.payment_reminders import generate_payment_reminders`
- ...

These imports only work when the folder `AI User Engagement Features` is the active working directory or is added to `sys.path`.

### AI-Powered Help

Imports follow a pattern such as:

- `from services.support.feature_guidance import get_feature_guidance`
- `from services.support.step_help import generate_step_help`
- `from services.support.help_articles import suggest_help_articles`

These imports only work when the `AI-Powered Help` directory is the active working directory or is added to `sys.path`.

### Improve AI POC

Imports use:

- `from config import Config`
- `from services.support.context_support import generate_context_help`
- `from services.support.faq_service import search_faq`
- `from services.support.response_quality import improve_response`

This is more fragile because the module expects sibling files in its own directory to be importable from that directory context.

## Route map

### Conflicting routes

The following route patterns are duplicated and conflict once these apps are merged into one deployment:

- `/`
- `/ai/help/context`
- `/ai/help/feature`
- `/ai/help/steps`
- `/ai/help/error`
- `/ai/help/articles`
- `/ai/help/automate`
- `/ai/help/escalate`

Those duplicates show that the apps were built as standalone prototypes and were never designed for shared deployment.

### Design impact

When all apps are exposed from one root Flask app, routes must be namespaced to avoid conflicts.

Recommended URL prefixes:

- Engagement app: `/engagement`
- Help app: `/help`
- Improved support app: `/support`

Examples:

- `/engagement/ai/personalized-recommendation`
- `/help/ai/help/context`
- `/support/ai/help/faq`

## Problems found

1. Multiple independent Flask apps exist in the same repo and each expects to run from its own folder.
2. The root repository does not contain a single production entry-point app.
3. Imports rely on the current working directory, which breaks when launched from repo root with `gunicorn app:app`.
4. Route collisions exist across the help/support apps.
5. The root `requirements.txt` is incomplete and does not include all sub-app dependencies.
6. The `Improve AI POC` UI route uses `render_template("index.html")` but the file is at the project root, not under a `templates` folder.
7. Python 3.14 compatibility is not guaranteed by this project stack because the stack was originally built for Python 3.11-era Flask and not explicitly validated against 3.14.
8. There is no single Render-compatible deployment plan or process definition.

## Recommended architecture

Use a single root application as the entry point:

- Root `app.py`
- Root `requirements.txt`
- Feature apps remain as reusable, independent modules
- The root app loads each existing Flask app from its child folder and mounts it behind a unique URL prefix
- Business logic remains in the original feature folders; the root app only orchestrates imports and routing

This keeps original functionality reusable without duplicating code.

## Recommended production entry point

Use:

- `app.py` at the repository root

This file should be the only production entry point used by Gunicorn.

Gunicorn command expected:

- `gunicorn app:app`

## Recommended Gunicorn command

```bash
gunicorn app:app
```

If a host/port is needed explicitly in deployment:

```bash
gunicorn --bind 0.0.0.0:$PORT app:app
```

## Recommended Render configuration

### Build command

```bash
pip install -r requirements.txt
```

### Start command

```bash
gunicorn app:app
```

### Runtime recommendation

Use a Python runtime version compatible with the project's Flask ecosystem, preferably:

- Python 3.11

Avoid using Python 3.14 as the default until the full dependency stack is explicitly validated in production.

## Exact file changes required

Planned file changes:

1. Create a new root-level `app.py` to serve as the unified entry point.
2. Update the root `requirements.txt` to include all needed packages for the merged app stack.
3. Add import-path compatibility so the child apps can be loaded from the repo root without `cd` commands.
4. Resolve route conflicts by mounting each app behind a unique prefix.
5. Fix template resolution for the `Improve AI POC` UI by pointing `template_folder` to the correct directory.
6. Keep all original feature logic untouched and reusable.

The final configuration will preserve the existing app functionality while making the whole project deployable from the repository root.
