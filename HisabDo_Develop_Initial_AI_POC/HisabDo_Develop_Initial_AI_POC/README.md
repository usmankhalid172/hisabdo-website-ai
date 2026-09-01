# HisabDo Initial AI POC

Lightweight prototype for the HisabDo AI Copilot.

## Run
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Example request
```json
{"message":"How do I add a customer?","language":"english"}
```

The included model provider is a mock adapter. Replace it with an approved local or API-based provider during integration.
